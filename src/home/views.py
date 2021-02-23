from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from products.models import Product


def index(request):
    return render(request, "home.html")


def search(request):
    search_text = request.POST.get('search')
    products = Product.objects.filter(title__icontains=search_text)
    context = {
        'products': products
    }
    return render(request, "home.html", context=context)


def category(request, category):
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, "home.html", context=context)
