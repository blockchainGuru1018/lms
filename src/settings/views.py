from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.urls import reverse_lazy
from django.urls import reverse

from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import Settings
from .forms import SettingsForm


class SettingsCreateView(SuccessMessageMixin, CreateView):
    model = Settings
    queryset = Settings.objects.all()
    template_name = "create.html"
    form_class = SettingsForm
    success_message = 'Doc successfully created!'
    error_message = 'Error saving the Doc, check fields below.'

    def get_success_url(self):
        return reverse ('settings:settings_update', kwargs={'pk': self.object.pk})


    def form_valid(self, form):
        #form = form.save(commit=False)
        form.instance.is_active = form.cleaned_data['is_active']
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(request, "Please correct the errors below and resubmit.")
        return render(request, template, context)



class SettingsDetaileView(TemplateView):
    template_name = "deatile.html"



class SettingsUpdateView(UpdateView):
    model = Settings
    queryset = Settings.objects.all()
    template_name = "create.html"
    form_class = SettingsForm
    success_message = 'Doc successfully created!'
    error_message = 'Error saving the Doc, check fields below.'

    def get_success_url(self):
        return reverse ('settings:settings_dashboard')



class SettingsDashboardView(ListView):
    template_name = "dashboard.html"
    model = Settings
    queryset = Settings.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SettingsDashboardView, self).get_context_data(**kwargs)
        context['settings_count'] = Settings.objects.all()
        return context
