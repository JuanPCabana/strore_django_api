from rest_framework import routers
from django.urls import path, include

# En este archivo se definen las rutas de la aplicación

urlpatterns = [
    path("products/", include("products.urls")),
]
