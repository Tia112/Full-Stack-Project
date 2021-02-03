from django.shortcuts import render
from products.models import Item

# Create your views here.

def index(request):

    products = Item.objects.all()
    context = {
        'products': products
    }
    return render(request, "home.html", context=context)

