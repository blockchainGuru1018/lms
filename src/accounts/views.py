from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
from django.views.generic.base import View
from django.views.generic.edit import CreateView

from .forms import RegisterForm
from django.views.generic.list import ListView

from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from accounts.models import UserProfile


class DashboardView(DetailView, LoginRequiredMixin):
    model = UserProfile
    template_name = 'accounts/dashboard.html'
    
    def get_object(self, queryset=None):
        
        self.object = self.request.user
        return self.object
    

class LoginView(LoginView):
    template_name = 'register/login.html'


class SignUpView(CreateView):
    template_name = 'register/signup.html'
    form_class = RegisterForm
    success_url = '/login/'


class LogoutView(View, LoginRequiredMixin):

    def get(self, request):
        logout(request)
        return redirect('/')


class UserList(ListView):
    template_name = 'user_list.html'
    model = UserProfile
