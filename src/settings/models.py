from django.db import models
from tinymce.models import HTMLField


class Settings(models.Model):
    unternehmens_name   = models.CharField(max_length=120)
    impressium          = HTMLField('impressium')
    datenschutz         = HTMLField('datenschutz')
    logo_img            = models.FileField(upload_to='settings/', null=True, blank=True)
    strasse             = models.CharField(max_length=120, blank=True)
    strasse2            = models.CharField(max_length=120, blank=True)
    ort                 = models.CharField(max_length=120, blank=True)
    land                = models.CharField(max_length=120, blank=True)
    telefon             = models.CharField(max_length=120, blank=True)
    email               = models.CharField(max_length=120, blank=True)
    plz                 = models.PositiveSmallIntegerField()
    is_active           = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_active)
