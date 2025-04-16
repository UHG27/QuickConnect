from django.db import models
from apps.empresa.models import Empresa

class Vacantes(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100)
    salario = models.CharField(max_length=50, blank=True)
    ubicacion = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.puesto} en {self.empresa.nombre}"
