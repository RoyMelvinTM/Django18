from django.http import HttpResponse
# Create your views here.


def index_adopcion(request):
    return HttpResponse("Soy la pagina principal de la app adopcion")
