from django.db import models

class Proveedor(models.Model):
    nombre_prov = models.CharField(max_length=100, default="Null", verbose_name ="Nombre")
    apellido_prov = models.CharField(max_length=100, default="", verbose_name ="Apellido")
    dni_prov = models.IntegerField(default=0, verbose_name ="Dni")
    
    def __str__(self):
        return self.nombre_prov


class Producto(models.Model):
    nombre_prod = models.CharField(max_length=100, default="Null", verbose_name ="Producto")
    precio_prod = models.IntegerField(default=0, verbose_name ="Precio")
    stock_actual_prod = models.IntegerField(default=0, verbose_name ="Stock")
    proveedor_prod = models.ForeignKey(Proveedor, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nombre_prod