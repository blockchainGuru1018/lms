from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from .views import (
                ProductListView,
                ProductCreateView,
                ProductUpdateView,
                ProductDetailView,
                ProductDeletelView,
                ShopListView,
                ShopDetaileView,
                ShopCreateView,
                )

app_name = 'shopping'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('detail/<pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('delete/<pk>/', ProductDeletelView.as_view(), name='product_delete'),
    path('shop/', ShopListView.as_view(), name='shop_list'),
    path('shop/produkt/<pk>', ShopDetaileView.as_view(), name='shop_detaile'),
    #path('shop/order/', ShopCreateView.as_view(), name='shop_create'),
    path('shop/success/', ShopCreateView.as_view(), name='shop_success'),
]
