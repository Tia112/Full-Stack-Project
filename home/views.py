from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from products.models import Product


def index(request):
    """
    Render Home Page of the Website
    :param request: GET
    :return: Renders home page
    """
    return render(request, "home.html", {"flag": False})


def search(request):
    """
    Renders products which contain search_text in their name or description
    :param request: POST
    :return: Products based on the search text given
    """
    search_text = request.POST.get("search")
    products = Product.objects.filter(title__icontains=search_text)

    flag = True
    return render(request, "home.html", {"products": products, "flag": flag})


def category(request, category):
    """
    Renders products which are a part of given category
    :param request: GET
    :param category: Product Category Type
    :return: Products based on the category given
    """
    products = Product.objects.filter(category=category)
    flag = True
    return render(request, "home.html", {"products": products, "flag": flag,
                                         "category": category})
