from django.db import models

class TestModel(models.Model):

    name_test = models.CharField(max_length=350, null=True, blank=True)
