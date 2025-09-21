from app.utils.console_util import limpiar_pantalla
from app.data.store import productos

from app.views.products_view import productos  
def mostrar_menu_control_stock():
    while True:
        limpiar_pantalla()
        print("\n--- CONTROL Y ALERTAS DE STOCK ---")
        STOCK_MINIMO = 5
        productos_bajo_stock = [p for p in productos if int(p['stock']) < STOCK_MINIMO]

        if not productos_bajo_stock:
            print("✅ No hay productos con stock bajo.")
        else:
            print("⚠️  Productos con stock bajo:")
            for p in productos_bajo_stock:
                print(f"  • {p['nombre']} (ID: {p['id']}) - Stock: {p['stock']} (mínimo: {STOCK_MINIMO})")

        print("\n1. Actualizar stock de un producto")
        print("2. Volver al menú principal")

        opcion = input("Selecciona una opción (1-2): ")

        if opcion == "1":
            actualizar_stock()
        elif opcion == "2":
            break
        else:
            print("❌ Opción no válida.")
            input("Presione Enter para continuar...")


def actualizar_stock():
    limpiar_pantalla()
    print("\n--- ACTUALIZAR STOCK ---")
    id_producto = input("Ingrese el ID del producto a actualizar: ")

    producto = None
    for p in productos:
        if p['id'] == id_producto:
            producto = p
            break

    if not producto:
        print("❌ Producto no encontrado.")
        input("Presione Enter para continuar...")
        return

    print(f"Producto: {producto['nombre']} - Stock actual: {producto['stock']}")
    cantidad = input("Ingrese la cantidad a agregar: ")

    try:
        cantidad = int(cantidad)
        producto['stock'] = str(int(producto['stock']) + cantidad) 
        print(f"✅ Stock actualizado: {producto['nombre']} ahora tiene {producto['stock']} unidades.")
    except ValueError:
        print("❌ Cantidad inválida.")

    input("Presione Enter para continuar...")
