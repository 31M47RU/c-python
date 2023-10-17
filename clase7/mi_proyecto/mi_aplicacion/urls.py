# en mi_aplicacion/urls.py
from django.urls import path
from .views import listar_entidades, detalle_entidad, crear_entidad

urlpatterns = [
    path('listar/', listar_entidades, name='listar_entidades'),
    path('<int:entidad_id>/', detalle_entidad, name='detalle_entidad'),
    path('crear/', crear_entidad, name='crear_entidad'),
]
