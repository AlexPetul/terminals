from rest_framework import serializers

from terminals.models import Terminal


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = "__all__"
