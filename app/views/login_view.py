from app.utils.console_util import limpiar_pantalla
from app.views.menu_home import mostrar_menu_home

def login_view():
    print("\n--- Iniciar Sesión ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    
    if username == "admin" and password == "1234":
        print("Inicio de sesión exitoso.")
        input("Presione Enter para continuar...")
        mostrar_menu_home()
       
    else:
        print("Usuario o contraseña incorrectos.")
        input("Presione Enter para intentar de nuevo...")
