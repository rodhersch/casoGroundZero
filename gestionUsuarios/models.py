from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    contrasenasdsadasa=models.CharField(max_length=50)
    comuna=models.CharField(max_length=50)


   