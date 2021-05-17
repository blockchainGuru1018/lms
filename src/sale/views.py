from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from shopping.models import Bestellung

class SaleListView(ListView):
    queryset = Bestellung.objects.all()
    model = Bestellung
    template_name = 'sale_list.html'
