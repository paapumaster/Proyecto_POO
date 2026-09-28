import sys
from negocios.sistema_noticias import SistemaNoticias

def menu_periodista(usuario):
    while True:
        print(f"\n--- MENÚ PERIODISTA ({usuario['nombre']}) ---")
        print("1. Crear borrador de noticia")
        print("2. Enviar noticia a revisión")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título de la noticia: ")
            contenido = input("Contenido: ")
            id_noticia = SistemaNoticias.crear_noticia_borrador(titulo, contenido, usuario['id'])
            if id_noticia:
                print(f"Noticia creada exitosamente en borrador (ID: {id_noticia}).")
            else:
                print("Error al crear la noticia.")
        elif opcion == '2':
            noticia_id = input("Ingrese el ID de la noticia a enviar a revisión: ")
            if SistemaNoticias.enviar_a_revision(noticia_id):
                print("Noticia enviada a revisión con éxito.")
            else:
                print("No se pudo cambiar el estado de la noticia.")
        elif opcion == '3':
            break

def menu_editor(usuario):
    while True:
        print(f"\n--- MENÚ EDITOR ({usuario['nombre']}) ---")
        print("1. Ver noticias pendientes de revisión")
        print("2. Publicar noticia")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            noticias = SistemaNoticias.obtener_noticias_en_revision()
            print("\n--- NOTICIAS EN REVISIÓN ---")
            for n in noticias:
                print(f"ID: {n['id']} | Título: {n['titulo']}")
        elif opcion == '2':
            noticia_id = input("Ingrese el ID de la noticia a publicar: ")
            if SistemaNoticias.publicar_noticia(noticia_id):
                print("¡Noticia publicada correctamente!")
            else:
                print("Error al publicar la noticia.")
        elif opcion == '3':
            break

def menu_lector(usuario):
    while True:
        print(f"\n--- MENÚ LECTOR ({usuario['nombre']}) ---")
        print("1. Leer noticias publicadas")
        print("2. Comentar una noticia")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            noticias = SistemaNoticias.obtener_noticias_publicadas()
            print("\n--- NOTICIAS PUBLICADAS ---")
            for n in noticias:
                print(f"ID: {n['id']} | {n['titulo']}\n   {n['contenido']}\n")
        elif opcion == '2':
            noticia_id = input("ID de la noticia a comentar: ")
            comentario = input("Escriba su comentario: ")
            if SistemaNoticias.comentar(noticia_id, usuario['id'], comentario):
                print("Comentario publicado.")
            else:
                print("Error al publicar comentario.")
        elif opcion == '3':
            break

def main():
    print("=== PLATAFORMA DE NOTICIAS ===")
    email = input("Email: ")
    password = input("Contraseña: ")

    usuario = SistemaNoticias.iniciar_sesion(email, password)
    if not usuario:
        print("Credenciales incorrectas.")
        return

    # Redirección según rol (1: Admin, 2: Periodista, 3: Editor, 4: Lector)
    if usuario['rol_id'] in (1, 2):
        menu_periodista(usuario)
    elif usuario['rol_id'] == 3:
        menu_editor(usuario)
    else:
        menu_lector(usuario)

if __name__ == '__main__':
    main()