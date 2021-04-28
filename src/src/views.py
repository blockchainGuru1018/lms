from django.shortcuts import render, redirect


def home_basic(request):
    return render(request, 'home.html')
