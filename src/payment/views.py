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
                use_default_delievery = data.get('use_default_delievery')
                if use_default_delievery:
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
                    postal_code = data.get('postal_code')

                    if is_form_valid([street_address1, shipping_country, postal_code]):
                        delivery_address = Address(
                            user=self.request.user,
                            street_address=street_address1,
                            apartment_address=street_address2,
                            country=shipping_country,
                            postal_code=postal_code
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
