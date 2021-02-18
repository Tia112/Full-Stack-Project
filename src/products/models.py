# Import Django libraries

from django.db import models
from django.shortcuts import render, reverse
from django.conf import settings
from django.contrib.auth import get_user_model


# Create Category Choices for Menu

CATEGORY_CHOICES = (
    ('SND', 'SUNDAES'),
    ('WFF', 'WAFFLES'),
    ('CRP', 'CREPES'),
    ('CHK', 'CHEESECAKE'),
    ('CKS', 'CAKES'),
    ('MLK', 'MILKSHAKES')
)

# Defining product item model

class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField()
    price = models.FloatField(default=0.00, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)

    def __str__(self):
        return self.title

    def absolute_url(self):
        return reverse("product", kwargs={'slug': self.slug})

    def add_to_cart(self):
        return reverse("add-to-cart", kwargs={'slug': self.slug})

    def remove_from_cart(self):
        return reverse("remove-from-cart", kwargs={'slug': self.slug})
