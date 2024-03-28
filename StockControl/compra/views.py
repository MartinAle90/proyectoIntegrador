from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor

# ----------------------------------------------------------------------------------------------------

# INDEX - Pagina de inicio
def index (request):
    return render(request, 'index.html')

# ----------------------------------------------------------------------------------------------------

# READ - Se muestra la lista con todos los proveedores
def lista_proveedores (request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

# READ - Se muestra la lista con todos los productos
def lista_productos (request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

# ----------------------------------------------------------------------------------------------------

# READ - Se muestra el detalle de un proveedor obtenido por id
def formulario_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'formulario_proveedor.html', {'proveedor':proveedor})

# READ - Se muestra el detalle de un producto obtenido por id
def formulario_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'formulario_producto.html', {'producto':producto})

# ----------------------------------------------------------------------------------------------------

# CREATE - Creacion de un proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        nombre_Prov = request.POST.get('nombre_Prov')
        apellido_Prov = request.POST.get('apellido_Prov')
        dni_Prov = request.POST.get('dni_Prov')
        Proveedor.objects.create(nombre_Prov=nombre_Prov, apellido_Prov=apellido_Prov, dni_Prov=dni_Prov)
        return redirect('lista_proveedores')
    return render(request, 'lista_proveedores.html')

# CREATE - Creacion de un productor
def crear_producto(request):
    if request.method == 'POST':
        nombre_Prod = request.POST.get('nombre_Prod')
        precio_Prod = request.POST.get('precio_Prod')
        stock_actual_Prod = request.POST.get('stock_actual_Prod')
        Producto.objects.create(nombre_Prod=nombre_Prod, precio_Prod=precio_Prod, stock_actual_Prod=stock_actual_Prod)
        return redirect('lista_productos')
    return render(request, 'lista_productos.html')

def formulario_crear_proveedor(request):
    return render(request, 'formulario_crear_proveedor.html')

def formulario_crear_producto(request):
    return render(request, 'formulario_crear_producto.html')

# ----------------------------------------------------------------------------------------------------

# UPDATE - Actualizar un proveedor
def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        nombre_Prov = request.POST.get('nombre_Prov')
        apellido_Prov = request.POST.get('apellido_Prov')
        dni_Prov = request.POST.get('dni_Prov')
        proveedor.nombre_Prov = nombre_Prov
        proveedor.apellido_Prov = apellido_Prov
        proveedor.dni_Prov = dni_Prov
        proveedor.save()
        return redirect('lista_proveedores')
    return render(request, 'lista_proveedores.html', {'proveedor': proveedor})

# UPDATE - Actualizar un productos
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        nombre_Prod = request.POST.get('nombre_Prod')
        precio_Prod = request.POST.get('precio_Prod')
        stock_actual_Prod = request.POST.get('stock_actual_Prod')
        proveedor = request.POST.get('proveedor')
        producto.nombre_Prod = nombre_Prod
        producto.precio_Prod = precio_Prod
        producto.stock_actual_Prod = stock_actual_Prod
        Proveedor.objects = proveedor
        producto.save()
        return redirect('lista_productos')
    return render(request, 'lista_productos.html', {'producto': producto})

# ----------------------------------------------------------------------------------------------------

# DELETE - Se encarga de eliminar un proveedor por id
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.delete()
    return redirect('lista_proveedores')

# DELETE - Se encarga de eliminar un proveedor por id
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')