from django.urls import path
from . import views

urlpatterns = [
    path('compras/productos/lista', views.mostrar_productos),
    path('compras/productos/crear/<str:inputnombre>/<str:inputapellido>/<int:inputedad>', views.crear_producto),
    path('compras/productos/actualizar/<int:id>', views.actualizar_producto),
    path('compras/productos/borrar/<int:id>', views.borrar_producto),
    
    path('compras/proveedores/lista', views.mostrar_proveedores),
    path('compras/proveedores/crear/<str:inputnombre>/<str:inputapellido>/<int:inputedad>', views.crear_proveedor),
    path('compras/proveedores/actualizar/<int:id>', views.actualizar_proveedor),
    path('compras/proveedores/borrar/<int:id>', views.borrar_proveedor),

]