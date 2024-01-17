from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def listadoProductos(req):
    return render(req,'listado_productos.html')

def crearProducto(req):
    return render(req,'crear_producto.html')