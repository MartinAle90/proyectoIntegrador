from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),

    path('compras/proveedores/lista', views.lista_proveedores, name='lista_proveedores'),
    path('compras/productos/lista', views.lista_productos, name='lista_productos'),
    
    path('compras/proveedores/<int:proveedor_id>/', views.formulario_proveedor, name='formulario_proveedor'),
    path('compras/productos/<int:producto_id>/', views.formulario_producto, name='formulario_producto'),
    
    path('compras/proveedores/formulario_crear_proveedor', views.formulario_crear_proveedor, name='formulario_crear_proveedor'),
    path('compras/proveedores/crear', views.crear_proveedor, name='crear_proveedor'),
    
    path('compras/productos/formulario_crear_producto', views.formulario_crear_producto, name='formulario_crear_producto'),
    path('compras/productos/crear', views.crear_producto, name='crear_producto'),
    
    path('compras/proveedores/<int:proveedor_id>/actualizar/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('compras/productos/<int:producto_id>/actualizar/', views.actualizar_producto, name='actualizar_producto'),
    
    path('compras/proveedores/<int:proveedor_id>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('compras/productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
]