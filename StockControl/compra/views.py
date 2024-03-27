from django.shortcuts import render, redirect
from .models import Producto, Proveedor

# Create Producto
def crear_producto(request, inputNombre, inputPrecio ,inputStock):
    nuevoProducto = Producto.objects.create(
        nombre_Prod = inputNombre,
        precio_Prod = inputPrecio,
        stock_actual_Prod = inputStock
    )
    nuevoProducto.save()
    return render(request, 'crearProducto.html', {'nuevoProducto': nuevoProducto})

def formulario_producto(request):

    return render(request, 'formularioAgregarProducto.html')

# Read Producto
def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listaProductos.html', {'productos': productos})

# Update Producto - Modificar instancia por id
def actualizar_producto(request, id):
    actualizarProducto = Producto.objects.get(id=id)
    actualizarProducto.nombre_Prod = "Marcos"
    actualizarProducto.save()
    return render(request, 'actualizarProducto.html', {'actualizarProducto': actualizarProducto})

# Delete Producto - Eliminar instancia por ID
def borrar_producto(request, id):
    userABorrar = Producto.objects.get(id = id) # igual a actualizar_usuario()
    userABorrar.delete() # funcion nativa de PY
    # igual a mostrar_usuarios()
    eliminarProducto = Producto.objects.all()
    return render(request, 'eliminarProducto.html', {'eliminarProducto': eliminarProducto})

# ----------------------------------------------------------------------------------------------------
# Create Proveedor
def crear_proveedor(request, inputNombre, inputApellido ,inputDni):
    nuevoProveedor = Proveedor.objects.create(
        nombre_Prov = inputNombre,
        apellido_Prov = inputApellido,
        dni_Prov = inputDni
    )
    nuevoProveedor.save()
    return render(request, 'crearProveedor.html', {'nuevoProveedor': nuevoProveedor})

def formulario_proveedor(request):

    return render(request, 'formularioAgregarProveedor.html')

# Read Proveedor
def mostrar_proveedores(request):
    listaProveedor = Proveedor.objects.all()
    return render(request, 'listaProveedor.html', {'listaProveedor': listaProveedor})

# Update Proveedor - Modificar instancia por id
def actualizar_proveedor(request, id):
    actualizarProveedor = Proveedor.objects.get(id=id)
    actualizarProveedor.nombre_Prod = "Marcos"
    actualizarProveedor.save()
    return render(request, 'actualizarProveedor.html', {'actualizarProveedor': actualizarProveedor})

# Delete Proveedor - Eliminar instancia por ID
def borrar_proveedor(request, id):
    eliminarProveedor = Proveedor.objects.get(id = id) # igual a actualizar_usuario()
    eliminarProveedor.delete() # funcion nativa de PY
    return render(request, 'eliminarProveedor.html', {'eliminarProveedor': eliminarProveedor})