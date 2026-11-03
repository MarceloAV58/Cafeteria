from django.db import models

# Create your models here.

class RedSocial(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'redsocial'
        verbose_name = 'Red Social'
        verbose_name_plural = 'Red Socials'
        ordering = ['name']

