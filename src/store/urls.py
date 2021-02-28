from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from home.views import index,search,category
from order.views import OrderSummaryView, OrderHistory
from payment.views import Checkout,PaymentPage
from products.views import ProductDetailView
from cart.views import add_to_cart,remove_from_cart,remove_single_item_from_cart

urlpatterns = [
    path('',index,name='index'),
    path('admin/',admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('search/',search,name='search'),
    path('category/<category>',category,name='category'),
    path('checkout/', Checkout.as_view(),name='checkout'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart,name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/',remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('order-history/', OrderHistory, name='order_history'),
    path('product/<slug>/',ProductDetailView.as_view(),name='product'),
    path('payment/<payment_option>/',PaymentPage.as_view(),name='payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

