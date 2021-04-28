from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from .views import CreateCheckoutSessionView, ProductLandingPageView, CancelView, SuccessView

app_name = 'shopping'

urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    #url(r'views/$', SignListView.as_view(), name='shopping_cart'),
    #url(r'^create/$', ShoppingCreateView.as_view(), name='shopping_create'),
    #url(r'^detaile/(?P<pk>\d+)/$', ShoppingDetailView.as_view(), name='shopping_detaile'),
    #url(r'^update/(?P<pk>\d+)/$', ShoppingUpdateView.as_view(), name='shopping_update'),
    #url(r'^delelet/(?P<pk>\d+)/$', ShoppingDeleteView.as_view(), name='shopping_delelet'),
    #url(r'^user/(?P<pk>\d+)/$', ShoppingCheckoutView.as_view(), name='shopping_user'),
]
