from django.db import models

class Proveedor(models.Model):
    nombre_Prov = models.CharField(max_length=100, default="", verbose_name ="Nombre")
    apellido_Prov = models.CharField(max_length=100, default="", verbose_name ="Apellido")
    dni_Prov = models.IntegerField(default=0, verbose_name ="Dni")
    
    def __str__(self):
        return self.nombre_Prov


class Producto(models.Model):
    nombre_Prod = models.CharField(max_length=100, default="", verbose_name ="Producto")
    precio_Prod = models.IntegerField(default=0, verbose_name ="Precio")
    stock_actual_Prod = models.IntegerField(default=0, verbose_name ="Stock")
    proveedor = models.ForeignKey(Proveedor, default="",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_Prod