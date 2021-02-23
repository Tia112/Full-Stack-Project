from django.conf import settings
from django.contrib import messages

from accounts.models import User
from order.models import OrderProduct, Order, Address
from products.models import Product
from payment.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

def is_form_valid(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

def generate_order_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

class Checkout(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
            }


delivery_address_queryset = Address.objects.filter(
    user=self.request.user, default=True)
            if delivery_address_queryset.exists():
                context.update(
                    {'default_delivery_address': delivery_address_queryset[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You don't have an Active Order")
            return redirect("checkout")

    def post(self, *args, **kwargs):
        print(self.request.POST)
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                data = form.cleaned_data
                use_default_delivery = data.get('use_default_delivery')
                if use_default_delivery:
                    address_queryset = Address.objects.filter(user=self.request.user,default=True)
                    if address_queryset.exists():
                        delivery_address = address_queryset[0]
                        order.delivery_address = delivery_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No Shipping Address Available")
                        return redirect('checkout')
                else:
                    street_address1 = data.get('street_address1')
                    street_address2 = data.get('street_address2')
                    shipping_country = data.get('shipping_country')
                    post_code = data.get('post_code')

                    if is_form_valid([street_address1, shipping_country, post_code]):
                        delivery_address = Address(
                            user=self.request.user,
                            street_address=street_address1,
                            apartment_address=street_address2,
                            country=shipping_country,
                            post_code=post_code
                        )
                        delivery_address.save()

                        order.delivery_address = delivery_address
                        order.save()

                        set_default_shipping = data.get('set_default_shipping')
                        if set_default_shipping:
                            delivery_address.default = True
                            delivery_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required Shipping Address Fields")

                payment_option = data.get('payment_option')

                if payment_option == 'S':
                    return redirect('payment', payment_option='stripe')
                else:
                    messages.warning(self.request, "Invalid payment option selected!!")
                    return redirect('checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You don't have an active order")
            return redirect("order-summary")

""" Payment Page with Stripe"""

class PaymentPage(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.delivery_address:
            context = {
                'order': order,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            }
            userprofile = self.request.user.user
            if userprofile.one_click_purchase:
                cards = stripe.Customer.list_sources(userprofile.customer_id,limit=3,object='card')
                card_list = cards['data']
                if len(card_list) > 0:
                    context.update({
                        'card': card_list[0]
                    })
            return render(self.request, "payment.html", context)
        else:
            messages.warning(
                self.request, "No Billing Address Added")
            return redirect("checkout")

def post(self, *args, **kwargs):

        form = PaymentForm(self.request.POST)

        userprofile = User.objects.get(user=self.request.user)
        if form.is_valid():
            data = form.cleaned_data
            token = data.get('stripeToken')
            save = data.get('save')
            use_default = data.get('use_default')

            if save:
                if userprofile.customer_id != '' and userprofile.customer_id is not None:
                    customer = stripe.Customer.retrieve(userprofile.customer_id)
                    customer.sources.create(source=token)

                else:
                    customer = stripe.Customer.create(email=self.request.user.email,)
                    customer.sources.create(source=token)
                    userprofile.stripe_customer_id = customer['id']
                    userprofile.one_click_purchase = True
                    userprofile.save()
            order = Order.objects.get(user=self.request.user, ordered=False)
            amount = int(order.get_total() * 100)

            try:
                if use_default or save:
                    charge = stripe.Charge.create(amount=amount,currency="gbp",customer=userprofile.stripe_customer_id)
                else:
                    charge = stripe.Charge.create(amount=amount,currency="gbp",source=token)


                payment = Payment()
                payment.stripe_bill_id = charge['id']
                payment.user = self.request.user
                payment.amt = order.get_total()
                payment.save()

                order_items = order.products.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

                order.ordered = True
                order.payment = payment
                order.orderid = generate_order_id()
                order.save()

                messages.success(self.request, "Your order was Successful!")
                return redirect("/")
   except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("/")

            except stripe.error.RateLimitError as e:
                messages.warning(self.request, "Rate limit error")
                return redirect("/")

            except stripe.error.InvalidRequestError as e:
                messages.warning(self.request, "Invalid parameters")
                return redirect("/")

            except stripe.error.AuthenticationError as e:
                messages.warning(self.request, "Not authenticated")
                return redirect("/")

            except stripe.error.APIConnectionError as e:
                messages.warning(self.request, "Network error")
                return redirect("/")

            except stripe.error.StripeError as e:
                messages.warning(self.request, "Something went wrong. Please try again. You haven't been Charged")
                return redirect("/")

            except Exception as e:
                messages.warning(self.request, "A serious issue occurred. We have been notifed.")
                return redirect("/")

        messages.warning(self.request, "Invalid data received")
        return redirect("/payment/stripe/")
