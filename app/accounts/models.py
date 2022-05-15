from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
