from django.db import models

class Persona(models.Model): 
# Definición del modelo Persona, que representa una persona en el sistema, representa una tabla en la base de datos
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)

class Reserva(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    cant_personas = models.IntegerField()

