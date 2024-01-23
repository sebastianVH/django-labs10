from django.shortcuts import render, HttpResponse,redirect
from inventario.models import Productos,Categorias

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
        categorias = Categorias.objects.all()
        ctx = {'categorias':categorias}
        return render(req,'crear_producto.html',ctx)
    else:
        nombre_producto = req.POST['nombre']
        precio_producto = req.POST['precio']
        stock_producto = req.POST['stock']
        categoria_producto = req.POST['categoria']
        #instanciar LA CATEGORIA, para luego almacenarla
        instancia_categoria = Categorias.objects.get(id=categoria_producto)
        #istanciamos un objeto de la CLASE, para poder luego almacenarlo
        nuevo_producto = Productos(nombre=nombre_producto,precio=precio_producto,stock=stock_producto,categoria=instancia_categoria)
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
    categorias = Categorias.objects.all()
    if req.method == "GET":
        ctx = {'producto':producto_a_editar,'categorias':categorias}
        return render(req,'editar_producto.html',ctx)
    else:
        nombre_nuevo = req.POST['nombre']
        precio_nuevo = req.POST['precio']
        stock_nuevo = req.POST['stock']
        categoria_nueva = req.POST['categoria']
        instancia_categoria = Categorias.objects.get(id=categoria_nueva)
        producto_a_editar.nombre = nombre_nuevo
        producto_a_editar.precio = precio_nuevo
        producto_a_editar.stock = stock_nuevo
        producto_a_editar.categoria = instancia_categoria
        producto_a_editar.save()
        return redirect('listado')
    
def crearCategoria(req):
    
    if req.method == "GET":
        return render(req,'crear_categoria.html')
    else:
        nombre_categoria = req.POST["nombre"]
        categoria = Categorias(nombre_categoria=nombre_categoria)
        categoria.save()
        return redirect('listado')