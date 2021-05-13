import json
import stripe
from datetime import datetime

from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.edit import FormView

from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Product, Bestellung

from .forms import ProductForm, BestellungForm

stripe.api_key = settings.STRIPE_SECRET_KEY

class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product/product_create.html'
    form_class = ProductForm
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.timestamp = datetime.now()
        return super(ProductCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse ('shopping:product_detail', kwargs={'pk': self.object.pk})


class ProductListView(ListView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'product/product_list.html'


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse ('shopping:product_detail', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        return obj


class ProductDeletelView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('shopping:product_list')


#Shop

class ShopListView(ListView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'shop/list.html'


class ShopCreateView(CreateView):
    form_class = BestellungForm
    template_name = 'shop/successfully.html'

    def form_valid(self, form):
        form_neu = form.save(commit=False)
        product = form.data['product']
        product = get_object_or_404(Product, id=product)
        form.product = product

        return super(ShopCreateView, self).form_valid(form)

#class ShopCreateView(CreateView):
    #form_class = BestellungForm
    #template_name = 'shop/successfully.html'

    #def get_success_url(self):
        #return reverse ('shopping:shop_list')

    #def form_valid(self, form):
        #object = form.instance.lecture = Lesson.objects.get(pk=self.kwargs['pk'])
        #self.object = form.save()
        #return super().form_valid(form)

    #def form_valid(self, form):
        #if 'order' in request.POST:
            #form = BestellungForm(request.POST, request.FILES)
            #if form.is_valid():
                #form = form.save(commit=False)
                #form.save()
        #return render(request, self.template_name)



class ShopDetaileView(DetailView):
    queryset = Product.objects.all()
    template_name = 'shop/detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        return obj

    def get_context_data(self, **kwargs):
        context = super(ShopDetaileView, self).get_context_data(**kwargs)
        context['form_neu'] = BestellungForm
        #context['lesson'] = self.get_object()
        return context












#
