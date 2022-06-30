from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=128)
    email = models.EmailField(db_index=True, unique=True)
    gender = models.CharField(
        choices=(
            ('F', 'female'),
            ('M', 'male')
        ), max_length=1, blank=True)
    birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
    ]

    objects = UserManager()

    def __str__(self):
        return self.email