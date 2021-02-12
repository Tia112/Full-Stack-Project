from django.db import models
from products.models import Product
from django_countries.fields import CountryField
from django.conf import settings

ADDRESS_TYPES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

User_Model = settings.AUTH_USER_MODEL


class Address(models.Model):
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, null=True, blank=True)
    apartment_address = models.CharField(max_length=100, null=True, blank=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPES)
    country = CountryField(multiple=False, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.user.username


class OrderProduct(models.Model):
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.qty} of {self.item.title}"

    def get_total_product_price(self):
        return self.qty * self.item.price

    def get_final_price(self):
        return self.get_total_product_price()


class Order(models.Model):
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', on_delete=models.CASCADE, blank=True, null=True)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.CASCADE, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
