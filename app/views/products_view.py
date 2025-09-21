from app.utils.console_util import limpiar_pantalla
from app.data.store import productos

#productos = []

def mostrar_menu_gestion_productos():
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE PRODUCTOS ---")
        print("1. Registrar nuevo producto")
        print("2. Listar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Buscar por código")
        print("6. Volver al menú principal")

        op = input("Selecciona una opción (1-6): ")

        if op == "1":
            registrar_producto()
        elif op == "2":
            listar_productos()
        elif op == "3":
            modificar_producto()
        elif op == "4":
            eliminar_producto()
        elif op == "5":
            buscar_producto_por_codigo()
        elif op == "6":
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")


def buscar_por_id(id_producto):
    for p in productos:
        if p['id'] == id_producto:
            return p
    return None


def registrar_producto():
    limpiar_pantalla()
    print("=== Registrar Producto ===")
    id_producto = input("ID del producto: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = input("Precio: ")
            
    while True:
        stock = input("Stock: ")
        if stock.isdigit():
            break
        else:
            print("El stock debe ser un número entero. Intente de nuevo.")

    producto = {
        'id': id_producto,
        'nombre': nombre,
        'descripcion': descripcion,
        'precio': precio,
        'stock': stock
    }

    productos.append(producto)
    print(f"\nProducto '{nombre}' registrado.")
    input("Presione Enter para continuar...")


def listar_productos():
    limpiar_pantalla()
    print("=== Listado de Productos ===")
    if not productos:
        print("No hay productos registrados.")
    else:
        for p in productos:
            print(f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}")
    input("\nPresione Enter para continuar...")


def buscar_producto_por_codigo():
    limpiar_pantalla()
    print("=== Buscar Producto ===")
    id_producto = input("Ingrese ID a buscar: ")
    p = buscar_por_id(id_producto)
    if p:
        print(f"\nEncontrado: {p['nombre']} - Precio: {p['precio']} - Stock: {p['stock']}")
    else:
        print("\nProducto no encontrado.")
    input("Presione Enter para continuar...")


def modificar_producto():
    limpiar_pantalla()
    print("=== Modificar Producto ===")
    id_producto = input("Ingrese ID del producto: ")
    p = buscar_por_id(id_producto)
    if not p:
        print("Producto no encontrado.")
        input("Presione Enter para continuar...")
        return

    print(f"\nModificando: {p['nombre']}")
    p['nombre'] = input(f"Nuevo nombre ({p['nombre']}): ") or p['nombre']
    p['descripcion'] = input(f"Descripción ({p['descripcion']}): ") or p['descripcion']
    p['precio'] = input(f"Precio ({p['precio']}): ") or p['precio']
    #p['stock'] = input(f"Stock ({p['stock']}): ") or p['stock']
    while True:
        nuevo_stock = input(f"Stock ({p['stock']}): ")
        if not nuevo_stock:
            break
        if nuevo_stock.isdigit():
            p['stock'] = nuevo_stock
            break
        else:
            print("El stock debe ser un número entero.")

    print(f"\nProducto actualizado: {p['nombre']}")
    input("Presione Enter para continuar...")


def eliminar_producto():
    limpiar_pantalla()
    print("=== Eliminar Producto ===")
    id_producto = input("Ingrese ID del producto: ")
    p = buscar_por_id(id_producto)
    if not p:
        print("Producto no encontrado.")
        input("Presione Enter para continuar...")
        return

    productos.remove(p)
    print(f"\nProducto '{p['nombre']}' eliminado.")
    input("Presione Enter para continuar...")
