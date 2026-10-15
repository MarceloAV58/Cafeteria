from django.contrib import admin
from .models import Producto
from .models import Servicio

admin.site.register(Producto)
admin.site.register(Servicio)

# Register your models here.
