from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    username = None

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, unique=True)
    is_manager = models.BooleanField(default=False)
    objects = UserManager()
