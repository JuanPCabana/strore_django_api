from rest_framework import routers
from django.urls import path, include

# this file is the main entry point for the urls

urlpatterns = [
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
]
