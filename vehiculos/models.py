from django.db import models
from django.utils.html import format_html
from django.core.validators import MaxValueValidator

class Vehiculo(models.Model):
    marca = models.CharField(max_length = 20, default='Ford')
    modelo = models.CharField(max_length = 100)
    serial_carroceria = models.CharField(max_length = 50)
    serial_motor = models.CharField(max_length = 50)
    carroceria = models.CharField(max_length = 20)
    precio = models.IntegerField(validators=[MaxValueValidator(2)])

title = models.CharField(max_lenght=50)
exceptional = models.BooleanField()

class Meta:
    permissions = [
        ('con permiso', 'tiene permiso genérico')
    ]

    def __str__(self):
        return self.titulo
