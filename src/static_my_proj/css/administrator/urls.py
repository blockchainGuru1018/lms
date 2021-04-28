from django.urls import path
from django.conf.urls import url

from .views import administrator

#administrator

app_name= 'administrator'
urlpatterns = [
    path('', administrator, name='administrator'),
]
