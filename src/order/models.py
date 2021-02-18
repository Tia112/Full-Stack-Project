from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from payment.models import Payment
from products.models import Product


ADDRESS_TYPE = (
    ('B', 'Billing_Address'),
    ('S', 'Shipping_Address'),
)

User_Model = settings.AUTH_USER_MODEL


class Address(models.Model):
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=100, null=True, blank=True)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPE)
    country = CountryField(multiple=False, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    default = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
       return f"{self.qty} of {self.item.title}"

    def get_sub_total(self):
        return self.qty * self.item.price

    def get_total(self):
        return self.get_sub_total()


class Order(models.Model):
    order_ref = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    billing_address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE(), blank=True, null=True)
    delivery_progress = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total()
        return total
