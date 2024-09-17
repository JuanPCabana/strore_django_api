from rest_framework import routers, permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django-store API Docs",
        default_version="v1",
        description="Api documentation for the Django-store project",
        contact=openapi.Contact(email="juanpx99@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)


# this file is the main entry point for the urls

urlpatterns = [
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
    # urls for the swagger documentation
    path("docs<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redocs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
