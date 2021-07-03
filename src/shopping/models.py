import random
import string

from django.conf import settings
from django.db import models
from django.urls.base import reverse
from tinymce.models import HTMLField

from accounts.models import UserProfile
from course.models import Course


class Product(models.Model):
    title = models.CharField(max_length=120, blank=True)
    preis = models.DecimalField(max_digits=6, decimal_places=2, default='0,00', blank=True)
    description = HTMLField('description')
    active = models.BooleanField(default=True)
    free_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    img = models.FileField(upload_to='course/', null=True, blank=True, default='placholder_vYebXbG.png')
    user = models.ForeignKey(UserProfile, related_name='user', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

    @property
    def stripe_price(self):
        return int(100 * self.preis)



class Bestellung(models.Model):
    firma = models.CharField(max_length=120, null=False, blank=False)
    vorname = models.CharField(max_length=120, blank=True)
    nachnahme = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=220, null=False, blank=False)
    adresse = models.CharField(max_length=120, null=False, blank=False)
    plz = models.PositiveSmallIntegerField()
    stadt = models.CharField(max_length=120, null=False, blank=False)
    land = models.CharField(max_length=120, null=False, blank=False)
    tax_nr = models.CharField(max_length=120, null=False, blank=False)
    tel = models.CharField(max_length=120, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.vorname

    @property
    def create_checkout_session_url(self):
        # return 'create-checkout-session'
        url = reverse('shopping:create_checkout_session', kwargs={'pk': self.pk})

        return url

    @property
    def stripe_success_url(self):
        return reverse('shopping:stripe_success', kwargs={'pk': self.pk})

    @property
    def stripe_cancel_url(self):
        return reverse('shopping:stripe_cancel', kwargs={'pk': self.pk})

    def get_domain_url(self, url, domain_url=None, scheme='https', port='443'):
        if not domain_url:
            domain_url = settings.PUBLIC_URL
        url = f'{scheme}://{domain_url}:{port}{url}'
        print(f'url:{url}...')
        return url

    @property
    def rand_password(self):
        return ''.join(
            [random.choice(string.printable) for _ in range(8)]
            )

    def create_user_from_order(self):
        new_user = UserProfile.objects.filter(email=self.email).first()
        if not new_user:
            new_user = UserProfile.objects.create_user(
                self.email, self.vorname,
                self.rand_password)

        return new_user
