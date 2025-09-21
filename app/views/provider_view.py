from app.utils.console_util import limpiar_pantalla
from app.data.store import proveedores  

def mostrar_menu_gestion_proveedores():
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE PROVEEDORES ---")
        print("1. Registrar proveedor")
        print("2. Listar proveedores")
        print("3. Modificar proveedor")
        print("4. Eliminar proveedor")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ")

        if op == "1":
            registrar_proveedor()
        elif op == "2":
            listar_proveedores()
        elif op == "3":
            modificar_proveedor()
        elif op == "4":
            eliminar_proveedor()
        elif op == "5":
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")


def buscar_proveedor_por_id(id_proveedor):
    for p in proveedores:
        if p['id'] == id_proveedor:
            return p
    return None


def registrar_proveedor():
    limpiar_pantalla()
    print("\n--- REGISTRAR PROVEEDOR ---")
    id_proveedor = input("ID: ")
    nombre = input("Nombre: ")
    contacto = input("Contacto: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    direccion = input("Dirección: ")

    proveedor = {
        'id': id_proveedor,
        'nombre': nombre,
        'contacto': contacto,
        'telefono': telefono,
        'email': email,
        'direccion': direccion
    }

    proveedores.append(proveedor)
    print(f"Proveedor '{nombre}' registrado.")
    input("Presione Enter para continuar...")


def listar_proveedores():
    limpiar_pantalla()
    print("\n--- LISTA DE PROVEEDORES ---")
    if not proveedores:
        print("No hay proveedores.")
    else:
        for p in proveedores:
            print(f"ID: {p['id']} | Nombre: {p['nombre']} | Contacto: {p['contacto']} | Teléfono: {p['telefono']}")
    input("\nPresione Enter para continuar...")


def modificar_proveedor():
    limpiar_pantalla()
    print("\n--- MODIFICAR PROVEEDOR ---")
    id_proveedor = input("ID del proveedor: ")
    p = buscar_proveedor_por_id(id_proveedor)

    if not p:
        print("Proveedor no encontrado.")
        input("Presione Enter para continuar...")
        return

    print(f"\nModificando: {p['nombre']}")
    p['nombre'] = input(f"Nuevo nombre ({p['nombre']}): ") or p['nombre']
    p['contacto'] = input(f"Contacto ({p['contacto']}): ") or p['contacto']
    p['telefono'] = input(f"Teléfono ({p['telefono']}): ") or p['telefono']
    p['email'] = input(f"Email ({p['email']}): ") or p['email']
    p['direccion'] = input(f"Dirección ({p['direccion']}): ") or p['direccion']

    print(f"Proveedor actualizado: {p['nombre']}")
    input("Presione Enter para continuar...")


def eliminar_proveedor():
    limpiar_pantalla()
    print("\n--- ELIMINAR PROVEEDOR ---")
    id_proveedor = input("ID del proveedor: ")
    p = buscar_proveedor_por_id(id_proveedor)

    if not p:
        print("Proveedor no encontrado.")
        input("Presione Enter para continuar...")
        return

    proveedores.remove(p)
    print(f"Proveedor '{p['nombre']}' eliminado.")
    input("Presione Enter para continuar...")
