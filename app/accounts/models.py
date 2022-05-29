from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    username = None

    name = models.CharField(max_length=40)
    team = models.ForeignKey(to="Team", on_delete=models.PROTECT, null=True)
    email = models.EmailField(max_length=254, unique=True)
    is_manager = models.BooleanField(default=False)
    objects = UserManager()


class Team(models.Model):
    name = models.CharField(max_length=50)
