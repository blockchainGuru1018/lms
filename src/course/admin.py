from django.contrib import admin
from .models import Course, Category, Participation

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Participation)
