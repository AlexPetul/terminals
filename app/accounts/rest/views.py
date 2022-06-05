from rest_framework import viewsets

from accounts.models import User

from ..permissions import ActionBasedPermission, UserRegisterPermission, UserRestrictScopePermission
from .serializers import UserCreateSerializer, UserSerializer


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
