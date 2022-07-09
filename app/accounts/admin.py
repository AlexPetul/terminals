from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    exclude = ("last_login", "user_permissions")


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ("name", "group")
