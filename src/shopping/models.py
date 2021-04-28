from django.db import models


class Product(models.Model):
    title           = models.CharField(max_length=120, blank=True)
    name            = models.CharField(max_length=100, blank=True)
    preis           = models.DecimalField(max_digits=6, decimal_places=2, default='0,00', blank=True)
    description     = models.TextField()
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
