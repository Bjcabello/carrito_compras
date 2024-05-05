from django.shortcuts import render, HttpResponse, redirect
from CarritoApp.models import Producto
from .carrito import Carrito

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {"productos": productos})

def add_product(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.add(producto)
    return redirect("tienda")

def delete_product(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.delete(producto)
    return redirect("tienda")

def subtract_product(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.subtract(producto)
    return redirect("tienda")

def clear_car(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect("tienda")


