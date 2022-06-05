from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from terminals.models import Terminal
from terminals.rest.serializers import TerminalSerializer


class TerminalsViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer
    permission_classes = (IsAuthenticated,)
