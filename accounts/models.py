from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings


class UserManager(BaseUserManager):
    def _create(self, email, password, name, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_user(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, name, **extra_fields)
    
    def create_superuser(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, name, **extra_fields)
    


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=20, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def str(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff
    
    def has_perm(self, obj=None):
        return self.is_staff


    def create_activation_code(self):
        code = get_random_string(20)
        self.activation_code = code
        self.save()
        return code

    def send_activation_code(self):
        activation_link = f'https://morning-depths-08273.herokuapp.com/account/activation/{self.activation_code}'
    
        send_mail(subject='Activation',
                message=activation_link,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.email],
                fail_silently=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'