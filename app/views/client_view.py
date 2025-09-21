from app.utils.console_util import limpiar_pantalla
from app.data.store import clientes 

def mostrar_menu_gestion_clientes():
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ")

        if op == "1":
            registrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            modificar_cliente()
        elif op == "4":
            eliminar_cliente()
        elif op == "5":
            break
        else:
            print("❌ Opción no válida.")
            input("Presione Enter para continuar...")


def buscar_cliente_por_id(id_cliente):
    for c in clientes:
        if c['id'] == id_cliente:
            return c
    return None


def registrar_cliente():
    limpiar_pantalla()
    print("\n--- REGISTRAR CLIENTE ---")
    id_cliente = input("ID: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    direccion = input("Dirección: ")

    cliente = {
        'id': id_cliente,
        'nombre': nombre,
        'telefono': telefono,
        'email': email,
        'direccion': direccion
    }

    clientes.append(cliente)
    print(f"✅ Cliente '{nombre}' registrado.")
    input("Presione Enter para continuar...")


def listar_clientes():
    limpiar_pantalla()
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("No hay clientes.")
    else:
        for c in clientes:
            print(f"ID: {c['id']} | Nombre: {c['nombre']} | Teléfono: {c['telefono']} | Email: {c['email']}")
    input("\nPresione Enter para continuar...")


def modificar_cliente():
    limpiar_pantalla()
    print("\n--- MODIFICAR CLIENTE ---")
    id_cliente = input("ID del cliente: ")
    c = buscar_cliente_por_id(id_cliente)

    if not c:
        print("❌ Cliente no encontrado.")
        input("Presione Enter para continuar...")
        return

    print(f"\nModificando: {c['nombre']}")
    c['nombre'] = input(f"Nuevo nombre ({c['nombre']}): ") or c['nombre']
    c['telefono'] = input(f"Teléfono ({c['telefono']}): ") or c['telefono']
    c['email'] = input(f"Email ({c['email']}): ") or c['email']
    c['direccion'] = input(f"Dirección ({c['direccion']}): ") or c['direccion']

    print(f"✅ Cliente actualizado: {c['nombre']}")
    input("Presione Enter para continuar...")


def eliminar_cliente():
    limpiar_pantalla()
    print("\n--- ELIMINAR CLIENTE ---")
    id_cliente = input("ID del cliente: ")
    c = buscar_cliente_por_id(id_cliente)

    if not c:
        print("❌ Cliente no encontrado.")
        input("Presione Enter para continuar...")
        return

    clientes.remove(c)
    print(f"✅ Cliente '{c['nombre']}' eliminado.")
    input("Presione Enter para continuar...")
