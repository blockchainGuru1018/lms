from django.urls import path
from .views import SaleListView
app_name = 'sale'

urlpatterns = [
    path('', SaleListView.as_view(), name='sale_list'),
    #path('update/<pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    #path('deletet/<pk>/', LessonDeleteView.as_view(), name='lesson_deletet'),
    #path('lecture/detaile/<pk>/', LectureDetailView.as_view(), name='lecture_detail'),
    #path('lecture/update/<pk>/', LectureUpdateView.as_view(), name='lecture_update'),
    #path('lecture/', LectureCreateView.as_view(), name='lecture_create'),
]
