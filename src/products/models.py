# Import Django libraries

from django.db import models
from django.shortcuts import reverse


# Create Category Choices for Menu

CATEGORY_CHOICES = (
    ('SND', 'SUNDAES'),
    ('WFF', 'WAFFLES'),
    ('CRP', 'CREPES'),
    ('CHK', 'CHEESECAKE'),
    ('CKS', 'CAKES'),
    ('MLK', 'MILKSHAKES')
)

# Create your models here.

# Definition for User Profile
class UserProfile(models.Model):
    user = models.OnetoOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    )

 def __str__(self):
        return self.title

# Defining product item model
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })
