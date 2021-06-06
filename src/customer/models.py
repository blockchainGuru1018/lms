from django.db import models

from django_tenants.models import DomainMixin, TenantMixin


class BaseDateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Client(TenantMixin, BaseDateModel):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)  # can login

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
    class Meta:
        abstract = False


class Domain(DomainMixin):

    class Meta:
        abstract = False
