from app.views.login_view import login_view

def main_menu():
    while True:
        print("\n=== Inventario de Productos ===")
        print("1. Iniciar Sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            login_view() 
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()
