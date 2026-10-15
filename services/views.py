from django.shortcuts import render
from .models import Producto, Servicio

# Create your views here.
def services(request):
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()
    context = {
        'productos': productos,
        'servicios': servicios
    }
    return render(request, template_name= 'core/services.html', context= context)


def lista_productos(request):
    productos = Producto.objects.all()

    context = {
        'productos': productos
    }

    return render(request, template_name='core/services.html', context= context)

def lista_servicios(request):
    servicios = Servicio.objects.all()

    context = {
        'servicios': servicios
    }

    return render(request, template_name= 'core/services.html', context= context)
