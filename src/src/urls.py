from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .views import home_basic

urlpatterns = [
    path('', home_basic, name='home_basic'),
    path('accounts/', include('accounts.urls')),
    path('course/', include('course.urls')),
    path('shopping/', include('shopping.urls')),
    path('lesson/', include('lesson.urls')),
    path('settings/', include('settings.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('sale/', include('sale.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
