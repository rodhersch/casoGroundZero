from django.shortcuts import render
from gestionUsuarios.models import Usuarios

# Create your views here.
def registrar_usuario(request):
    return render(request, "registrate.html")

def registrar(request):
    if request.method=="POST":
        nombre=request.POST["fullname"]
        apellido=request.POST["lastname"]
        email=request.POST["email"]
        contrasenia=request.POST["password"]
        comuna=request.POST["comuna"]
        
        nuevo_usuario=Usuarios(
            nombre=nombre,
            apellido=apellido,
            email=email,
            contrasenia=contrasenia,
            comuna=comuna
        )
        nuevo_usuario.save()
    return render(request, "registrate.html")