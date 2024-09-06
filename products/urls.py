from rest_framework import routers
from .api.views import ProductViewSet

router = routers.DefaultRouter()

router.register(r"", ProductViewSet, basename="products")

urlpatterns = router.urls
