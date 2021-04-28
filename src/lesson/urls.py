from django.urls import path
from .views import LessonDetailView, LessonUpdateView, LessonDeleteView, LectureCreateView, LectureDetailView, LectureUpdateView

app_name = 'lesson'

urlpatterns = [
    path('detail/<pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('update/<pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('deletet/<pk>/', LessonDeleteView.as_view(), name='lesson_deletet'),
    path('lecture/detaile/<pk>/', LectureDetailView.as_view(), name='lecture_detail'),
    path('lecture/update/<pk>/', LectureUpdateView.as_view(), name='lecture_update'),
    path('lecture/', LectureCreateView.as_view(), name='lecture_create'),
]
