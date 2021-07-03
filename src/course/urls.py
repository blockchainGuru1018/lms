from .views import *

from django.urls import path

app_name = 'course'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    # url(r'^user/(?P<pk>\d+)/$', CourseUserView.as_view(), name='course_detail'),
    path('material/<pk>/', CourseMaterialView.as_view(), name='course_material'),
    path('update/<pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('deletet/<pk>/deletet/', CourseDeleteView.as_view(), name='course_deletet'),
    path('category/update/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/deletet/<pk>/', CategoryDeleteView.as_view(), name='category_deletet'),
    # User View
    path('view/lesson/<lesson_id>/', user_view, name='user_lesson_single'),
    path('view/lesson/', user_view, name='user_lesson'),
    path('view/cours/<pk>/', CourseUserSingleView.as_view(), name='user_single'),
]
