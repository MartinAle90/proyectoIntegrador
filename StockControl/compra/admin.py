from django.contrib import admin
from .models import Proveedor, Producto

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    # ordenar por 'id', si se antepone el simbolo menos (-) orden descendente
    # sin simbolo, es orden ascendente.
    ordering = ['id']
    # campos o columanas que se muestran en la grilla
    # En list_display podemos agregar 'id' para mostrar en la grilla
    list_display = ['nombre_Prov', 'apellido_Prov', 'dni_Prov']
    # Estables los campos sobre los cuales vamos a realizar la busqueda
    search_fields = ["nombre_Prov", 'apellido_Prov', "dni_Prov"]

class ProductoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['nombre_Prod', 'precio_Prod', 'stock_actual_Prod', 'proveedor']
    search_fields = ["nombre_Prod", "precio_Prod"]

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)