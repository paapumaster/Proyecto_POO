from auxiliares.mensajes import MSG_SALIDA
from presentacion.menu_categorias import menu_gestion_categorias
from presentacion.menu_noticias import menu_gestion_noticias
from presentacion.menu_usuarios import menu_gestion_usuarios


def mostrar_menu_principal(sesion: dict) -> None:
    while True:
        print(f"\n=== MENÚ PRINCIPAL | {sesion['nombre']} ({sesion['rol']}) ===")
        print("1. Gestionar usuarios")
        print("2. Gestionar noticias")
        print("3. Gestionar categorías")
        print("0. Cerrar sesión y salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_gestion_usuarios()
        elif opcion == "2":
            menu_gestion_noticias()
        elif opcion == "3":
            menu_gestion_categorias()
        elif opcion == "0":
            print(MSG_SALIDA)
            break
        else:
            print("Opción no válida.")