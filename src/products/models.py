# Import Django libraries

from django.db import models
from django.shortcuts import reverse


# Create Categroy Choices for Menu

CATEGORY_CHOICES = (
    ('SND', 'SUNDAES'),
    ('WFF', 'WAFFLES'),
    ('CRP', 'CREPES'),
    ('COK', 'COOKIES'),
    ('CKS', 'CAKES'),
    ('MLK', 'MILKSHAKES')
)

# Create your models here.

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
