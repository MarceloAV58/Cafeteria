from django.contrib import admin
from .models import Persona
from .models import Categoria
from .models import Publicacion

admin.site.register(Persona)
admin.site.register(Categoria)
admin.site.register(Publicacion)

# Register your models here.
