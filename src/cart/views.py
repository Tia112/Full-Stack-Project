from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone

from products.models import Product
from order.models import OrderProduct, Order, Address


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product.qty += 1
            order_product.save()
            messages.info(request, "Product quantity was updated.")
            return redirect("order-summary")
        else:
            order.products.add(order_product)
            messages.info(request, "Product added to cart.")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "Product added to cart.")
        return redirect("order-summary")


@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product, user=request.user, ordered=False)[0]
            order.products.remove(order_product)
            order_product.delete()
            messages.info(request, "Product removed to cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "Product not found in cart.")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("product", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product, user=request.user, ordered=False)[0]
            if order_product.qty > 1:
                order_product.qty -= 1
                order_product.save()
            else:
                order.products.remove(order_product)
            messages.info(request, "Product quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "Not in cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "No Active Order")
        return redirect("product", slug=slug)
