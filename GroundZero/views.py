from django.http import HttpResponse
# from datetime
from django.template import Template, Context as ctx

def index(request):
    index_page=open("GroundZero/templates/index.html", encoding="utf8")
    plt=Template(index_page.read())
    index_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artistas(request):
    artistas_page=open("GroundZero/templates/artistas.html", encoding="utf8")
    plt=Template(artistas_page.read())
    artistas_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artista(request):
    artista_page=open("GroundZero/templates/artista.html", encoding="utf8")
    plt=Template(artista_page.read())
    artista_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artista2(request):
    artista2_page=open("GroundZero/templates/artista2.html", encoding="utf8")
    plt=Template(artista2_page.read())
    artista2_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artista3(request):
    artista3_page=open("GroundZero/templates/artista3.html", encoding="utf8")
    plt=Template(artista3_page.read())
    artista3_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artista4(request):
    artista4_page=open("GroundZero/templates/artista4.html", encoding="utf8")
    plt=Template(artista4_page.read())
    artista4_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artista5(request):
    artista5_page=open("GroundZero/templates/artista5.html", encoding="utf8")
    plt=Template(artista5_page.read())
    artista5_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

def artista6(request):
    artista6_page=open("GroundZero/templates/artista6.html", encoding="utf8")
    plt=Template(artista6_page.read())
    artista6_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)

