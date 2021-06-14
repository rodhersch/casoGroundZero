from django.http import HttpResponse
# from datetime
from django.template import Template, Context as ctx

def index(request):
    index_page=open("GroundZero/templates/index.html")
    plt=Template(index_page.read())
    index_page.close()
    document=plt.render(ctx())

    return HttpResponse(document)