from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import Team, User

from ..permissions import ActionBasedPermission, UserRegisterPermission, UserRestrictScopePermission
from .serializers import TeamSerializer, UserCreateSerializer, UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=["GET"])
    def users(self, request, *args, **kwargs):
        instance: Team = self.get_object()
        serializer_data = UserSerializer(instance=instance.users, many=True)
        return Response(serializer_data.data)

    @action(detail=True, methods=["GET"])
    def terminals(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        UserRestrictScopePermission: ["update", "partial_update", "destroy", "list", "retrieve"],
        UserRegisterPermission: ["create"],
    }

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer

        return super().get_serializer_class()
