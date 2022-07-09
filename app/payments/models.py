from django.db import models

from terminals.models import Terminal


class Payment(models.Model):
    terminal = models.ForeignKey(to=Terminal, on_delete=models.CASCADE)
