from django.urls import path
from . import views

urlpatterns = [
    path("chau/", views.chau),
]
