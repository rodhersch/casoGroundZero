from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50, null = True)
    apellido=models.CharField(max_length=50, null = True)
    email=models.EmailField(null = True)
    contrasenia=models.CharField(max_length=50, null = True)
    comuna=models.CharField(max_length=50, null = True)


   