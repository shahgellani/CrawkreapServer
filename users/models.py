from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from .usermanager import UserManager


class User(AbstractBaseUser):
    username = models.CharField(blank=True, null=True , max_length=25)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    """

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    date_joined = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField(upload_to='uploads', blank=True)

