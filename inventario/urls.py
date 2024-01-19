from django.urls import path,include
from inventario.views import listadoProductos,crearProducto,eliminarProducto,editarProducto

urlpatterns = [
    path('listado/',listadoProductos,name='listado'),
    path('crear/',crearProducto,name='crear'),
    path('eliminar/<id>',eliminarProducto,name='eliminar'),
    path('editar/<id>',editarProducto,name='editar'),
]