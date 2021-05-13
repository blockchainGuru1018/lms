from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from .views import (
            SettingsCreateView,
            SettingsDetaileView,
            SettingsUpdateView,
            SettingsDashboardView
            )

app_name = 'settings'

urlpatterns = [

    path('create/', SettingsCreateView.as_view(), name='settings_create'),
    path('detaile/', SettingsDetaileView.as_view(), name='settings_detaile'),
    path('update/<pk>/', SettingsUpdateView.as_view(), name='settings_update'),
    path('dashboard/',SettingsDashboardView.as_view(),name='settings_dashboard')
    #path('detail/<pk>/', ProductDetailView.as_view(), name='product_detail'),
    #path('delete/<pk>/', ProductDeletelView.as_view(), name='product_delete'),
    #path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    #path('', ProductLandingPageView.as_view(), name='landing-page'),
    #path('cancel/', CancelView.as_view(), name='cancel'),
    #path('success/', SuccessView.as_view(), name='success'),

]
