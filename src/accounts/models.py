from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django_tenants.models import DomainMixin, TenantMixin


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class UserProfile(TenantMixin, AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    is_active   = models.BooleanField(default=True) # can login
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser
    timestamp   = models.DateTimeField(auto_now_add=True)
    is_teacher  = models.BooleanField(default=False)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
    class Meta:
        abstract = False
    
    TPL_DIR = 'accounts/emails/new_users'
    
    def send_new_user_email(self, order_id):
        """send email to new created user"""
        from shopping.models import Bestellung
        order = get_object_or_404(Bestellung, pk=order_id)
        payload = dict(user=self, order=order)
        
        subject = render_to_string(
            f'{self.TPL_DIR}/subject.html',
            payload
            )
        body = render_to_string(
            f'{self.TPL_DIR}/body.html',
            payload
            )
        
        self.email_user(subject, body)

class Domain(DomainMixin):
    class Meta:
        abstract = False
