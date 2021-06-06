from datetime import datetime
import logging

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
import stripe

from shopping.tasks.checkout import create_user_after_checkout

from .forms import ProductForm, BestellungForm
from .models import Product, Bestellung

logger = logging.getLogger(__name__)

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


# Shop
class ShopListView(ListView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'shop/list.html'


# Stripe payment view
class ShopCreateView(CreateView):
    form_class = BestellungForm
    template_name = 'shop/detail.html'

    def get_success_url(self):
        return reverse ('shopping:shop_success_view', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        ctx = CreateView.get_context_data(self, **kwargs)
        ctx['object'] = self.get_product()
        ctx['form_neu'] = kwargs.get('form', self.form_class())
        return ctx
    
    def get_product(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Product, id=pk)

    def form_valid(self, form):
        form.save(commit=False)
        self.object = self.get_product()
        form.product = self.object
        form.save()
        
        return redirect(self.get_success_url())


# Stripe Store important data for billing
class ShopSuccessView(DetailView):
    queryset = Bestellung.objects.all()
    template_name = 'shop/successfully.html'

    def get_context_data(self, **kwargs):
        ctx = DetailView.get_context_data(self, **kwargs)
        ctx['settings'] = settings
        return ctx
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Bestellung, pk=pk)
        return obj

# class ShopCreateView(CreateView):
    # form_class = BestellungForm
    # template_name = 'shop/successfully.html'

    # def get_success_url(self):
        # return reverse ('shopping:shop_list')

    # def form_valid(self, form):
        # object = form.instance.lecture = Lesson.objects.get(pk=self.kwargs['pk'])
        # self.object = form.save()
        # return super().form_valid(form)

    # def form_valid(self, form):
        # if 'order' in request.POST:
            # form = BestellungForm(request.POST, request.FILES)
            # if form.is_valid():
                # form = form.save(commit=False)
                # form.save()
        # return render(request, self.template_name)


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
        # context['lesson'] = self.get_object()
        return context


@csrf_exempt
def create_checkout_session(request, pk):
    obj = get_object_or_404(Bestellung, pk=pk)
    domain_url = request.tenant.domain_url
    scheme = request.scheme
    port = request.META.get('SERVER_PORT', 80)
    
    data = {
        'payment_method_types': ['card'],
        'line_items': [{
          'price_data': {
            'currency': 'eur',
            'product_data': {
              'name': obj.product.title,
            },
            'unit_amount': obj.product.stripe_price,
          },
          'quantity': 1,
        }],
        'mode': 'payment',
        'success_url': obj.get_domain_url(obj.stripe_success_url, domain_url, scheme, port=port),
        'cancel_url': obj.get_domain_url(obj.stripe_cancel_url, domain_url, scheme, port=port),
    }
    logger.info(f'data:{data}...')
    session = stripe.checkout.Session.create(
        **data
    )

    return JsonResponse(dict(id=session.id))


# Stripe successfull page
class SripeCancelView(DetailView):
    queryset = Bestellung.objects.all()
    template_name = 'shop/stripe_failed.html'
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Bestellung, pk=pk)
        return obj


class SripeSuccessView(SripeCancelView):
    template_name = 'shop/stripe_success.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # create user and send email in this
        # it will be an async call as
        """ 
        create_user_after_checkout.apply_async(
            args=[self.object.pk]
            )
        """
        create_user_after_checkout(self.object.pk)
        return SripeCancelView.get(self, request, *args, **kwargs)
