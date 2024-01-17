from django.urls import path,include
from inventario.views import listadoProductos,crearProducto

urlpatterns = [
    path('listado/',listadoProductos),
    path('crear/',crearProducto),
]