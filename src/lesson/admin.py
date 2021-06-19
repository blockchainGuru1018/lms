from django.contrib import admin
from .models import Lesson, Lecture
from .models import LessonVenue

admin.site.register(Lesson)
admin.site.register(Lecture)


class LessonVenueAdmin(admin.ModelAdmin):
    search_fields = ('lesson__name',)
    raw_id_fields = ['participations', 'lesson', ]

    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        # check send student about this lesson
        
        if obj.is_active and form.initial.get('is_active', False) != obj.is_active:
            from .tasks.lesson import send_student_active_lesson_task
            
            send_student_active_lesson_task.apply_async(
                args=[obj.pk]
                )
            

admin.site.register(LessonVenue, LessonVenueAdmin)
