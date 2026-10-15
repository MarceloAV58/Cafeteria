from django.shortcuts import render, get_object_or_404
from .models import Publicacion, Categoria
# Create your views here.
def blog(request):
    publicaciones = Publicacion.objects.all()
    categorias = Categoria.objects.all()
    contexto = {
        'publicaciones': publicaciones,
        'categorias': categorias
    }
    return render(request, template_name= 'core/blog.html', context= contexto)

def categorias(request, category_name):
    categorias = Categoria.objects.all()
    categoria_seleccionada = get_object_or_404(Categoria, nombre__iexact=category_name)

    publicaciones = Publicacion.objects.filter(categoria=categoria_seleccionada)
    contexto = {
        'publicaciones': publicaciones,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada
    }
    return render(request, template_name= 'core/blog.html', context= contexto)