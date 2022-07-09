from django.db import models

from terminals.models import Terminal


CELL_STATUSES = (("OK", "OK"), ("ERROR", "ERROR"))


class Cell(models.Model):
    terminal = models.ForeignKey(to=Terminal, on_delete=models.CASCADE)
    state = models.CharField(max_length=5, choices=CELL_STATUSES)
