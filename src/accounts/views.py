from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView


from .forms import RegisterForm, LoginForm
from .models import UserProfile

#def login(request):
#    return render(request, 'register/login.html')

#def logout(request):
#    return render(request, 'register/logout.html')

#def signup(request):
#    return render(request, 'register/signup.html')


class LoginView(TemplateView):
    form_class = LoginForm
    template_name = 'register/login.html'
    success_url = '/login/'


class SignUpView(CreateView):
    template_name = 'register/signup.html'
    form_class = RegisterForm
    success_url = '/login/'



class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('/')
