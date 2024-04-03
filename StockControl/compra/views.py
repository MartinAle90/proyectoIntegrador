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
    proveedores = Proveedor.objects.all()
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'formulario_producto.html', {'producto':producto, 'proveedores':proveedores})

# ----------------------------------------------------------------------------------------------------

# CREATE - Creacion de un proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        nombre_prov = request.POST.get('nombre_prov')
        apellido_prov = request.POST.get('apellido_prov')
        dni_prov = request.POST.get('dni_prov')
        Proveedor.objects.create(nombre_prov=nombre_prov, apellido_prov=apellido_prov, dni_prov=dni_prov)
        return redirect('lista_proveedores')
    return render(request, 'lista_proveedores.html')

# CREATE - Creacion de un productor
def crear_producto(request):
    if request.method == 'POST':
        nombre_prod = request.POST.get('nombre_prod')
        precio_prod = request.POST.get('precio_prod')
        stock_actual_prod = request.POST.get('stock_actual_prod')
        proveedor_prod = request.POST.get('proveedor_prod')
        Producto.objects.create(
            nombre_prod=nombre_prod,
            precio_prod=precio_prod,
            stock_actual_prod=stock_actual_prod,
            proveedor_prod=Proveedor(extract_digits(proveedor_prod))
            )
        return redirect('lista_productos')
    return render(request, 'lista_productos.html')

def formulario_crear_proveedor(request):
    return render(request, 'formulario_crear_proveedor.html')

def formulario_crear_producto(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'formulario_crear_producto.html', {'proveedores':proveedores})

# ----------------------------------------------------------------------------------------------------

# UPDATE - Actualizar un proveedor
def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        nombre_prov = request.POST.get('nombre_prov')
        apellido_prov = request.POST.get('apellido_prov')
        dni_prov = request.POST.get('dni_prov')
        proveedor.nombre_prov = nombre_prov
        proveedor.apellido_prov = apellido_prov
        proveedor.dni_prov = dni_prov
        proveedor.save()
        return redirect('lista_proveedores')
    return render(request, 'lista_proveedores.html', {'proveedor': proveedor})

# UPDATE - Actualizar un productos
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        nuevo_nombre_prod = request.POST.get('nombre_prod')
        nuevo_precio_prod = request.POST.get('precio_prod')
        nuevo_stock_actual_prod = request.POST.get('stock_actual_prod')
        nuevo_proveedor = request.POST.get('proveedor_prod')
        producto.nombre_prod = nuevo_nombre_prod
        producto.precio_prod = nuevo_precio_prod
        producto.stock_actual_prod = nuevo_stock_actual_prod
        producto.proveedor_prod = Proveedor(extract_digits(nuevo_proveedor))
        producto.save()
        return redirect('lista_productos')
    return render(request, 'lista_productos.html', {'producto': producto} )

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

# ----------------------------------------------------------------------------------------------------

# funcion que se usa para la extraccion de los digitos de un string
def extract_digits(text):
    digits = []
    for char in text:
        if char.isdigit():
            digits.append(char)
    return ''.join(digits)