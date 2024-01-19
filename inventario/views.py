from django.shortcuts import render, HttpResponse,redirect
from inventario.models import Productos

# Create your views here.
def listadoProductos(req):
    #crear el listado de productos
    productos = Productos.objects.all() #traer TODA una lista de productos => [Azucar,Yerba,Harina] || <QuerySet [<Productos: Harina>, <Productos: Yerba>, <Productos: Azucar>]>
    #crearemos el contexto: la representacion que va a tener un elemento DENTRO de un html: el ctx se representa mediante un DICCIONARIO, en el cual, la llave sera la manera en la que lo REPRESENTAREMOS dentro del html, y el valor sera EL CONTENIDO de esa representacion
    contexto = {'productos':productos}
    return render(req,'listado_productos.html',contexto)

def crearProducto(req):
    #capturar LOS DATOS DEL FORMULARIO
    if req.method == 'GET':
        return render(req,'crear_producto.html')
    else:
        nombre_producto = req.POST['nombre']
        precio_producto = req.POST['precio']
        stock_producto = req.POST['stock']
        #istanciamos un objeto de la CLASE, para poder luego almacenarlo
        nuevo_producto = Productos(nombre=nombre_producto,precio=precio_producto,stock=stock_producto)
        #ejecutamos el metodo SAVE, para que se almacene en la DDBB
        nuevo_producto.save()
        return redirect('listado')

def eliminarProducto(req,id):
    #primero debo BUSCAR el producto (el objeto)
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('listado')

def editarProducto(req,id):
    producto_a_editar = Productos.objects.get(id=id)
    if req.method == "GET":
        ctx = {'producto':producto_a_editar}
        return render(req,'editar_producto.html',ctx)
    else:
        nombre_nuevo = req.POST['nombre']
        precio_nuevo = req.POST['precio']
        stock_nuevo = req.POST['stock']
        producto_a_editar.nombre = nombre_nuevo
        producto_a_editar.precio = precio_nuevo
        producto_a_editar.stock = stock_nuevo
        producto_a_editar.save()
        return redirect('listado')