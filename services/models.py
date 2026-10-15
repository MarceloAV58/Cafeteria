from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    eslogan = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen_nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'productos'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['nombre']


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    image_nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'servicios'
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['nombre']
