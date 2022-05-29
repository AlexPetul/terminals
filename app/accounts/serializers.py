from rest_framework import serializers

from .models import Team, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("password",)
        model = User


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Team
