# en tus vistas
from django.shortcuts import render, redirect, get_object_or_404
from .models import Entidad
from .forms import EntidadForm  # Asegúrate de tener un formulario definido

def listar_entidades(request):
    entidades = Entidad.objects.all()
    return render(request, 'mi_aplicacion/listar_entidades.html', {'entidades': entidades})


def detalle_entidad(request, entidad_id):
    entidad = get_object_or_404(Entidad, id=entidad_id)
    return render(request, 'mi_aplicacion/detalle_entidad.html', {'entidad': entidad})


def crear_entidad(request):
    if request.method == 'POST':
        form = EntidadForm(request.POST)
        if form.is_valid():
            # Guardar la entidad en la base de datos
            entidad = form.save()
            # Puedes realizar otras acciones aquí, si es necesario
            return redirect('listar_entidades')  # Redirige a la lista de entidades
    else:
        form = EntidadForm()

    return render(request, 'mi_aplicacion/crear_entidad.html', {'form': form})

