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
