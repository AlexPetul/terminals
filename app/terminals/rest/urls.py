from rest_framework.routers import DefaultRouter

from terminals.rest.views import TerminalsViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"terminals", TerminalsViewSet, basename="terminal")

urlpatterns = router.urls
