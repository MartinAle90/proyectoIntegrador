from django import forms
from django.forms import ModelForm
from models import Producto, Proveedor

class formularioProducto(ModelForm):
    model = Producto
    fields = ['nombe']