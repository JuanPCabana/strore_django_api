from rest_framework import routers
from .api.views import OrderViewSet

router = routers.DefaultRouter()

router.register(r"", OrderViewSet, basename="orders")

urlpatterns = router.urls
