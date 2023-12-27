from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    mensaje="""
    <h1>Inicio</h1>
    """
    return HttpResponse(mensaje)


def saludo(request):
    mensaje = "Hola UNTELS..."
    return HttpResponse(mensaje)
