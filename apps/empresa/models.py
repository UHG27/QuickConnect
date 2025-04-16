from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='empresas/', blank=True, null=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
