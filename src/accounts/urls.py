from django.urls import path, include
from .views import SignUpView, LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
