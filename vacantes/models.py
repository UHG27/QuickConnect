from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='empresas/', blank=True, null=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Vacante(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100)
    salario = models.CharField(max_length=50, blank=True)
    ubicacion = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.puesto} en {self.empresa.nombre}"
