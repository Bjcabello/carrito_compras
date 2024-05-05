from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    categoria = models.CharField(max_length=40)
    image = models.ImageField(default=timezone.now, verbose_name='Imagen', upload_to='images')
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} -> {self.precio}"

