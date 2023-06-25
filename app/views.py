from django.shortcuts import redirect, render
from .models import Producto

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

#ventas

def productos(request):
    pro=Producto.objects.all()
    return render(request, 'ventas/productos.html',{'pro':pro})

def agregar(request):
    return render(request, 'ventas/agregar.html')

def agregarrec(request):
    x=request.POST['nombre']
    y=request.POST['descripcion']
    z=request.POST['precio']
    imagen=request.FILES.get('imagen')
    pro=Producto(nombre=x,descripcion=y,precio=z,imagen=imagen)
    pro.save()
    return redirect("/productos")

def eliminar(request,id):
    pro=Producto.objects.get(id=id)
    pro.delete()
    return redirect("/productos")

def actualizar(request,id):
    pro=Producto.objects.get(id=id)
    return render(request,'ventas/actualizar.html',{'pro':pro})

def actualizarrec(request,id):
    x=request.POST['nombre']
    y=request.POST['descripcion']
    z=request.POST['precio']
    imagen=request.FILES.get('imagen')
    pro=Producto.objects.get(id=id)
    pro.nombre=x
    pro.descripcion=y
    pro.precio=z
    pro.imagen=imagen
    pro.save()
    return redirect("/productos")