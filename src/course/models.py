import datetime
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db import models
#from tinymce import HTMLField

class Course(models.Model):
    name = models.CharField(max_length=120)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    #is_active = models.BooleanField(default=False)
    img = models.FileField(upload_to='course/', null=True, blank=True)
    description = models.TextField(blank=True, null=True, max_length=1024)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    #participants = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course:course_update", kwargs={"pk":self.pk})



class Category(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    order = models.IntegerField()

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse("course:category_update", kwargs={"pk":self.pk})


    class Meta():
        ordering = ['order']
