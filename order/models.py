from django.db import models
from payment.models import Payment
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField

User_Model = settings.AUTH_USER_MODEL


class Address(models.Model):
    """
    Address class to store Address saved by the user for delivery
    """
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, null=True, blank=True)
    apartment_address = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(multiple=False, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.user.username


class OrderProduct(models.Model):
    """
    OrderProduct class which hold info & quantity of each product in the cart.
    """
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.qty} of {self.product.title}"

    def get_total_product_price(self):
        return self.qty * self.product.price

    def get_final_price(self):
        return self.get_total_product_price()


class Order(models.Model):
    """
    Model class for creating Customer Order Objects
    Each order is attached to a particular address and a particular user
    Each order has many to many relation with OrderProduct class which hold
    quantity of each product in the cart.
    Note PEP8 standards could not be followed for some defintions
    """
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    orderid = models.CharField(max_length=20, blank=True, null=True)
    products = models.ManyToManyField(OrderProduct)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    delivery_address = models.ForeignKey(Address, related_name='delivery_address', on_delete=models.CASCADE,
                                         blank=True, null=True)
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.products.all():
            total += order_item.get_final_price()
        return total
