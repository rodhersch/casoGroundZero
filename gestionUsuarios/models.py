from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    contraseña=models.CharField(max_length=50)
    comuna=models.CharField(max_length=50)


   