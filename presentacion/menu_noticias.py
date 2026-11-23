from auxiliares.constantes import ESTADOS_NOTICIA
from auxiliares.validaciones import entero_positivo
from negocio.noticia_servicio import (
    actualizar_noticia,
    borrar_noticia,
    buscar_noticias,
    crear_noticia,
    obtener_noticias,
)


def menu_gestion_noticias() -> None:
    while True:
        print("\n--- GESTIÓN DE NOTICIAS ---")
        print("1. Crear noticia")
        print("2. Listar noticias")
        print("3. Buscar noticia por título")
        print("4. Modificar noticia")
        print("5. Eliminar noticia")
        print("0. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            print("Estados disponibles:", ", ".join(ESTADOS_NOTICIA))
            estado = input("Estado [borrador]: ").strip() or "borrador"
            ok, msg = crear_noticia(titulo, contenido, estado)
            print(msg)

        elif opcion == "2":
            noticias = obtener_noticias()
            if not noticias:
                print("No hay noticias registradas.")
                continue
            for n in noticias:
                print(f"[{n.id}] ({n.estado}) {n.titulo}")

        elif opcion == "3":
            termino = input("Texto a buscar en el título: ")
            resultados = buscar_noticias(termino)
            if not resultados:
                print("No se encontraron noticias.")
                continue
            for n in resultados:
                print(f"[{n.id}] ({n.estado}) {n.titulo}")

        elif opcion == "4":
            noticia_id = entero_positivo(input("ID de noticia a modificar: "))
            if not noticia_id:
                print("ID inválido.")
                continue
            titulo_txt = input("Nuevo título (Enter para no cambiar): ").strip()
            contenido_txt = input("Nuevo contenido (Enter para no cambiar): ").strip()
            estado_txt = input("Nuevo estado (Enter para no cambiar): ").strip()

            titulo = titulo_txt if titulo_txt else None
            contenido = contenido_txt if contenido_txt else None
            estado = estado_txt if estado_txt else None

            ok, msg = actualizar_noticia(noticia_id, titulo, contenido, estado)
            print(msg)

        elif opcion == "5":
            noticia_id = entero_positivo(input("ID de noticia a eliminar: "))
            if not noticia_id:
                print("ID inválido.")
                continue
            ok, msg = borrar_noticia(noticia_id)
            print(msg)

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")