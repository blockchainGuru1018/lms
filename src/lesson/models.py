
from django.db import models
from django.shortcuts import get_object_or_404

from course.models import Category


class DatefieldBaseModel(models.Model):
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()
    
    class Meta:
        abstract = True


class Lesson(DatefieldBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    
    link_url = models.URLField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True, max_length=1024)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['order']
    

class Lecture(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to='lecture/img/', default='teacheravatar.jpg')
    lecture = models.ForeignKey(Lesson, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.name


class LessonVenue(DatefieldBaseModel):
    participations = models.ManyToManyField("course.Participation",
                                        related_name='lesson_venues')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default='1')
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.lesson)
    
    @classmethod
    def send_student_active_lesson(cls, pk):
        model = get_object_or_404(cls, pk=pk)
        model.send_active_lesson()

    def send_active_lesson(self):
        """send all student of this venue about the available lesson
        """
        participation = self.participations.select_related(
            'course',
            'user',).all()
        for participation in participation:
            participation.user.send_available_lesson_email(
                self.lesson, participation.course
                )
            
