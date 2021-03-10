from django.db import models
from django.conf import settings
User_Model = settings.AUTH_USER_MODEL


class Payment(models.Model):
    """
    Payment class stores the details about the purchase like bill id, amount
    paid and the user who placed the order.
    """
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    stripe_bill_id = models.CharField(max_length=50)
    user = models.ForeignKey(
        User_Model, on_delete=models.SET_NULL, blank=True, null=True)
    amt = models.FloatField(default=0.00, blank=True, null=True)

    def __str__(self):
        return self.user.username
