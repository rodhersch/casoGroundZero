from django.shortcuts import render
from gestionUsuarios.models import Usuarios
from gestionUsuarios.models import Contactos

# Create your views here.
def registrar_usuario(request):
    return render(request, "registrate.html")

def registrar(request):
    if request.method=="POST":
        if request.POST["password"] != request.POST["confirm_password"]:
            return render(request, "registrate.html")
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

def registrar_solicitud_contacto(request):
    return render(request, "contacto.html")

def registrar_solicitud(request):
    if request.method=="POST":
        nombre=request.POST["fullname"]
        apellido=request.POST["lastname"]
        email=request.POST["email"]
        comuna=request.POST["comuna"]
        comentario=request.POST["comments"]           
        nuevo_contacto=Contactos(
            nombre=nombre,
            apellido=apellido,
            email=email,
            comuna=comuna,
            comentario=comentario
        )
        nuevo_contacto.save()
    return render(request, "contacto.html")
