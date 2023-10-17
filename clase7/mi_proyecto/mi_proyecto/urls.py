# en mi_proyecto/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_aplicacion/', include('mi_aplicacion.urls')),
]
