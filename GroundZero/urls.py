"""GroundZero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GroundZero.views import index, artistas, artista, artista2, artista3, artista4, artista5, artista6, esculturas, manualidades, nosotros, pinturas, usuarios, mostrar
from gestionUsuarios.views import registrar_usuario, registrar, registrar_solicitud_contacto, registrar_solicitud
from django.conf.urls import include,url
from django.conf import settings
from django.contrib.staticfiles.views import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('registrar_usuario/', registrar_usuario),
    path('registrar/', registrar),
    path('artistas/', artistas),
    path('artista/', artista),
    path('artista2/', artista2),
    path('artista3/', artista3),
    path('artista4/', artista4),
    path('artista5/', artista5),
    path('artista6/', artista6),
    path('registrar_solicitud_contacto/', registrar_solicitud_contacto),
    path('esculturas/', esculturas),
    path('manualidades/', manualidades),
    path('nosotros/', nosotros),
    path('pinturas/', pinturas),
    path('usuarios/', usuarios),
    path('registrar_solicitud/', registrar_solicitud),
    path('mostrar/', mostrar),
    
]


#urlpatterns += staticfiles_urlpatterns()