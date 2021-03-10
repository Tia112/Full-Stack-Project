from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Product


class ProductDetailView(DetailView):
    """
    Inherited BASE class DetailView
    Renders Detail Page for a particular product.
    """
    model = Product
    template_name = "product.html"
