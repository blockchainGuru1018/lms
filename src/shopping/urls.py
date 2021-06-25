from django.urls import path

from shopping.views import create_checkout_session

from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeletelView,
    ShopListView,
    ShopDetaileView,
    ShopCreateView,
    ShopSuccessView,
    SripeSuccessView,
    SripeCancelView,
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
    path('shop/success/<pk>', ShopCreateView.as_view(), name='shop_success'),
    path('shop/success/<pk>/done', ShopSuccessView.as_view(), name='shop_success_view'),
    path('shop/success/<pk>/create-checkout-session', create_checkout_session, name='create_checkout_session'),
    path('shop/sripe-success/<pk>', SripeSuccessView.as_view(), name='stripe_success'),
    path('shop/sripe-cancel/<pk>', SripeCancelView.as_view(), name='stripe_cancel'),

]
