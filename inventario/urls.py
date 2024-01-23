from django.urls import path,include
from inventario.views import *

urlpatterns = [
    path('',listadoProductos,name='listado'),
    path('crear/',crearProducto,name='crear'),
    path('eliminar/<id>',eliminarProducto,name='eliminar'),
    path('editar/<id>',editarProducto,name='editar'),
    path('crear_categoria',crearCategoria,name='crear_categoria')
]