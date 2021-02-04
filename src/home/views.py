from django.shortcuts import render
from products.models import Item

# Create your views here.

def index(request):

    products = Item.objects.all()
    context = {
        'products': products
    }
    return render(request, "home.html", context=context)

# Search function for Navbar
def search(request):

    search_text = request.POST.get('search')
    products = item.objects.filter(title_icontains=search_text)
    context = {
        'products': products
    }
    return render(request, "home.html", context=context)

