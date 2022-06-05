from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet, basename="api-users")

urlpatterns = [
    path("auth/token", TokenObtainPairView.as_view(), name="obtain_token"),
    path("auth/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
] + router.urls
