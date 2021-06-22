from django.db import models
from django.urls import reverse

from course.models import Course
from django.contrib.auth.models import User


from tinymce.models import HTMLField

from accounts.models import UserProfile

class Product(models.Model):
    title           = models.CharField(max_length=120, blank=True)
    preis           = models.DecimalField(max_digits=6, decimal_places=2, default='0,00', blank=True)
    description     = HTMLField('description')
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    course          = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    img             = models.FileField(upload_to='course/', null=True, blank=True, default='placholder_vYebXbG.png')
    user            = models.ForeignKey(UserProfile, related_name='user', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title


class Bestellung(models.Model):
    firma       = models.CharField(max_length=120, blank=True)
    #vorname     = models.CharField(max_length=120, blank=True)
    #nachnahme   = models.CharField(max_length=120, blank=True)
    #email       = models.CharField(max_length=220, blank=True)
    #adresse     = models.CharField(max_length=120, blank=True)
    #plz         = models.PositiveSmallIntegerField()
    #stadt       = models.CharField(max_length=120, blank=True)
    #land        = models.CharField(max_length=120, blank=True)
    #tax_nr      = models.PositiveSmallIntegerField()
    #tel         = models.CharField(max_length=120, blank=True)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.firma

    def get_absolute_url(self):
        return reverse("shopping:shop_list")

    #, kwargs={"pk":self.pk}
