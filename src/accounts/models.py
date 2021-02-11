from django.db.models.signals import post_save
from django.conf import settings
from django.db import models

# Create your models here.

# Definition for User Profile

User_Model = settings.AUTH_USER_MODEL,

class User(models.Model):
    user = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=55, blank=True, null=True)
    one_click_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

def user_data_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = User.objects.create(user=instance)

post_save.connect(user_data_receiver, sender=User_Model)
