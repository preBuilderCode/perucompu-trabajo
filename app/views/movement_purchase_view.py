from app.utils.console_util import limpiar_pantalla
from app.data.store import productos, clientes, movimientos  

def mostrar_menu_gestion_movimientos_compras():
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN MOVIMIENTOS/COMPRAS ---")
        print("1. Registrar nueva compra")
        print("2. Listar movimientos")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            registrar_compra()
        elif opcion == "2":
            listar_movimientos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")


def registrar_compra():
    limpiar_pantalla()
    print("\n--- REGISTRAR COMPRA ---")

    # Buscar producto
    id_producto = input("ID del producto: ")
    producto = next((p for p in productos if p['id'] == id_producto), None)
    if not producto:
        print("Producto no encontrado.")
        input("Presione Enter para continuar...")
        return

    # Buscar cliente
    id_cliente = input("ID del cliente: ")
    cliente = next((c for c in clientes if c['id'] == id_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        input("Presione Enter para continuar...")
        return

    # Cantidad
    try:
        cantidad = int(input("Cantidad a comprar: "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        print("Cantidad inválida.")
        input("Presione Enter para continuar...")
        return

    # Verificar stock
    stock_actual = int(producto['stock'])
    if cantidad > stock_actual:
        print(f"Stock insuficiente. Solo hay {stock_actual} unidades.")
        input("Presione Enter para continuar...")
        return

    # Actualizar stock
    producto['stock'] = str(stock_actual - cantidad)

    # Registrar movimiento
    movimiento = {
        'cliente_id': id_cliente,
        'cliente_nombre': cliente['nombre'],
        'producto_id': id_producto,
        'producto_nombre': producto['nombre'],
        'cantidad': cantidad,
        'fecha': 'HOY'
    }
    movimientos.append(movimiento)

    print(f"Compra registrada: {cliente['nombre']} compró {cantidad} de {producto['nombre']}.")
    input("Presione Enter para continuar...")


def listar_movimientos():
    limpiar_pantalla()
    print("\n--- LISTA DE MOVIMIENTOS ---")
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        for m in movimientos:
            print(f"Cliente: {m['cliente_nombre']} | Producto: {m['producto_nombre']} | Cantidad: {m['cantidad']} | Fecha: {m['fecha']}")
    input("\nPresione Enter para continuar...")
