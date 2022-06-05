from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import AllowAny


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access based on view method
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, "action_permissions", {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class UserRestrictScopePermission(permissions.BasePermission):
    pass


class UserRegisterPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return True
