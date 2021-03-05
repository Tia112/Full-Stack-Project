from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from products.models import Product


def index(request):
    return render(request, "home.html", {"flag": False})


def search(request):
    search_text = request.POST.get("search")
    products = Product.objects.filter(title__icontains=search_text)

    flag = True
    return render(request, "home.html", {"products": products, "flag": flag})


def category(request, category):
    products = Product.objects.filter(category=category)
    flag = True
    return render(request, "home.html", {"products": products, "flag": flag, "category": category})
