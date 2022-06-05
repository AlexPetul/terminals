from django.db import models


class Terminal(models.Model):
    owner = models.ForeignKey(to="accounts.User", on_delete=models.PROTECT)
    address = models.CharField(max_length=120)
    description = models.TextField(max_length=2000)
    state = models.CharField(max_length=10, choices=(("ACTIVE", "Active"), ("BLOCKED", "Blocked")))
