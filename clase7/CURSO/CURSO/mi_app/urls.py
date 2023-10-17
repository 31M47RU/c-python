from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("file/", views.return_file),
    path("dynamic-file/", views.return_dynamic_file),
]
