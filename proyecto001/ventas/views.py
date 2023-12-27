from django.shortcuts import render, redirect
from .models import Usuario, Productos, venta
from django.contrib import messages
from django.db.models import Q
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from flask import Flask, render_template, request
##from post.api.serializers import PostSerializer
# Create your views here.
def base_view(request):
    return render(request, 'base.html')

def realizarVentas_view(request):
    busqueda = request.GET.get("buscar")
    productos = Productos.objects.all()
    mensaje_error = None
    if busqueda: 
        productos = Productos.objects.filter(
            Q(codigo__icontains = busqueda) |
            Q(descripcion__icontains = busqueda) |
            Q(stock__icontains = busqueda)
        ).distinct()
                # Verificar si no se encontraron productos
        if not productos:
            mensaje_error = 'Producto no encontrado'

    return render(request, 'realizar_ventas.html', {'productos': productos, 'mensaje_error': mensaje_error})


def ventas_view(request):
    ventas = venta.objects.all()
    context = {'ventas' : ventas,
               }

    return render(request, 'ventas.html', context)

def productos_view(request):
    productos = Productos.objects.all()
    context = {
        'productos' : productos,
    }
    return render(request, 'productos.html', context)

def agregar(request):
    codigo = request.POST['codigo']
    producto = request.POST['producto']
    cantidad = request.POST['cantidad']
    precio = request.POST['precio']
    resultado = request.POST['resultado']
    registro = venta.objects.create(
        codigo=codigo, producto=producto, cantidad=cantidad, PrecioUnitario=precio, total=resultado)
    messages.success(request, 'productos registrados')
    return redirect('/')

def emitir_proforma(request):
    ventas = venta.objects.all()
    context = {'ventas' : ventas,
               }
    return render(request, 'proforma.html',context)

def eliminar_productos(request):
    # Elimina todos los productos de la venta
    venta.objects.all().delete()
    messages.success(request, 'La lista de productos ha sido eliminada correctamente.')
    return redirect('ventas')  # Redirige a la página donde se agregan productos