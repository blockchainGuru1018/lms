from django.contrib import admin
from .models import UserProfile
from django.conf import settings


admin.site.register(UserProfile)
