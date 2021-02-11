from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
