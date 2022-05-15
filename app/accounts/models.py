from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, unique=True)
    is_manager = models.BooleanField(default=False)
