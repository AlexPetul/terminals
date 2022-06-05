from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("email", "password")
        model = User

    def validate_password(self, value):
        validate_password(password=value, user=self.instance)

        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("password",)
        model = User
