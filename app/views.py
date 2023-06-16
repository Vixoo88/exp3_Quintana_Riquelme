from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def informacion(request):
    return render(request , 'informacion.html')

def galeria(request):
    return render(request , 'galeria.html')

def formulario(request):
    return render(request , 'formulario.html')

def api(request):
    return render(request , 'api.html')