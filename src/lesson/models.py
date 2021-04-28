from django.db import models
from course.models import Category

class Lesson(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    name        = models.CharField(max_length=120)
    update      = models.DateTimeField(auto_now=True)
    create      = models.DateTimeField(auto_now_add=True)
    order       = models.IntegerField()
    link_url    = models.URLField(null=False, blank=False)
    is_active   = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True, max_length=1024)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['order']

class Lecture(models.Model):
    name        = models.CharField(max_length=150)
    description = models.CharField(max_length=120, blank=True)
    photo       = models.ImageField(upload_to='lecture/img/', default='teacheravatar.jpg')
    lecture      = models.ForeignKey(Lesson, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.name
