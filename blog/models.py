from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        db_table = 'personas'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        ordering = ['nombre']

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'categorias'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nombre']

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(default='')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicaciones'
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicaciones'

        ordering = ['categoria__nombre', '-fecha_creacion']

        indexes = [
            models.Index(fields=['categoria', 'persona']),
        ]