from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, PermissionsMixin
from django.db import models

from .managers import UserManager


class Team(models.Model):
    name = models.CharField(max_length=50)
    group = models.OneToOneField(to=Group, on_delete=models.PROTECT)

    @property
    def users(self):
        print(self.group)
        return self.group.user_set.all()


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    username = None

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    team = models.ForeignKey(to=Team, on_delete=models.PROTECT)
    objects = UserManager()
