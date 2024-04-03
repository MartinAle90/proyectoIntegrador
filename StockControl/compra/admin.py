from django.contrib import admin
from .models import Proveedor, Producto

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    # ordenar por 'id', si se antepone el simbolo menos (-) orden descendente
    # sin simbolo, es orden ascendente.
    ordering = ['id']
    # campos o columanas que se muestran en la grilla
    # En list_display podemos agregar 'id' para mostrar en la grilla
    list_display = ['id', 'nombre_prov', 'apellido_prov', 'dni_prov']
    # Estables los campos sobre los cuales vamos a realizar la busqueda
    search_fields = ["nombre_prov", 'apellido_prov', "dni_prov"]

class ProductoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id','nombre_prod', 'precio_prod', 'stock_actual_prod', 'proveedor_prod']
    search_fields = ["nombre_prod", "precio_prod"]

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)