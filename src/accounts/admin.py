from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import UserProfile



@admin.register(UserProfile)
class UserProfileAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = (
        'email', 
        'is_active',
        'staff',
        'admin',
        'is_teacher',
        'full_name', )
