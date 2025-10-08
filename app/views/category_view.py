from app.utils.console_util import limpiar_pantalla
from app.data.store import categorias  

def mostrar_menu_gestion_categorias():
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE CATEGORÍAS ---")
        print("1. Registrar categoría")
        print("2. Listar categorías")
        print("3. Modificar categoría")
        print("4. Eliminar categoría")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ")

        if op == "1":
            registrar_categoria()
        elif op == "2":
            listar_categorias()
        elif op == "3":
            modificar_categoria()
        elif op == "4":
            eliminar_categoria()
        elif op == "5":
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")


def buscar_categoria_por_id(id_categoria):
    for c in categorias:
        if c['id'] == id_categoria:
            return c
    return None


def registrar_categoria():
    limpiar_pantalla()
    print("\n--- REGISTRAR CATEGORÍA ---")
    id_categoria = input("ID: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")

    categoria = {
        'id': id_categoria,
        'nombre': nombre,
        'descripcion': descripcion
    }

    categorias.append(categoria)
    print(f"Categoría '{nombre}' registrada.")
    input("Presione Enter para continuar...")


def listar_categorias():
    limpiar_pantalla()
    print("\n--- LISTA DE CATEGORÍAS ---")
    if not categorias:
        print("No hay categorías.")
    else:
        for c in categorias:
            print(f"ID: {c['id']} | Nombre: {c['nombre']} | Descripción: {c['descripcion']}")
    input("\nPresione Enter para continuar...")


def modificar_categoria():
    limpiar_pantalla()
    print("\n--- MODIFICAR CATEGORÍA ---")
    id_categoria = input("ID de la categoría: ")
    c = buscar_categoria_por_id(id_categoria)

    if not c:
        print("Categoría no encontrada.")
        input("Presione Enter para continuar...")
        return

    print(f"\nModificando: {c['nombre']}")
    c['nombre'] = input(f"Nuevo nombre ({c['nombre']}): ") or c['nombre']
    c['descripcion'] = input(f"Descripción ({c['descripcion']}): ") or c['descripcion']

    print(f"Categoría actualizada: {c['nombre']}")
    input("Presione Enter para continuar...")


def eliminar_categoria():
    limpiar_pantalla()
    print("\n--- ELIMINAR CATEGORÍA ---")
    id_categoria = input("ID de la categoría: ")
    c = buscar_categoria_por_id(id_categoria)

    if not c:
        print("categoría no encontrada.")
        input("Presione Enter para continuar...")
        return

    categorias.remove(c)
    print(f"Categoría '{c['nombre']}' eliminada.")
    input("Presione Enter para continuar...")
