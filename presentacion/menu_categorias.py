from auxiliares.validaciones import entero_positivo
from negocio.categoria_servicio import (
    actualizar_categoria,
    borrar_categoria,
    buscar_categoria,
    crear_categoria,
    obtener_categorias,
)


def menu_gestion_categorias() -> None:
    while True:
        print("\n--- GESTIÓN DE CATEGORÍAS ---")
        print("1. Crear categoría")
        print("2. Listar categorías")
        print("3. Buscar categoría por ID")
        print("4. Modificar categoría")
        print("5. Eliminar categoría")
        print("0. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la categoría: ")
            slug_txt = input("Slug (Enter para generar automáticamente): ").strip()
            slug = slug_txt if slug_txt else None
            ok, msg = crear_categoria(nombre, slug)
            print(msg)

        elif opcion == "2":
            categorias = obtener_categorias()
            if not categorias:
                print("No hay categorías registradas.")
                continue
            print("\nID | Nombre | Slug")
            for c in categorias:
                print(f"{c.id} | {c.nombre} | {c.slug}")

        elif opcion == "3":
            cat_id = entero_positivo(input("ID de categoría: "))
            if not cat_id:
                print("ID inválido.")
                continue
            cat = buscar_categoria(cat_id)
            if not cat:
                print("Categoría no encontrada.")
            else:
                print(f"[{cat.id}] {cat.nombre} (slug: {cat.slug})")

        elif opcion == "4":
            cat_id = entero_positivo(input("ID de categoría a modificar: "))
            if not cat_id:
                print("ID inválido.")
                continue
            nombre_txt = input("Nuevo nombre (Enter para no cambiar): ").strip()
            slug_txt = input("Nuevo slug (Enter para no cambiar): ").strip()
            nombre = nombre_txt if nombre_txt else None
            slug = slug_txt if slug_txt else None
            ok, msg = actualizar_categoria(cat_id, nombre, slug)
            print(msg)

        elif opcion == "5":
            cat_id = entero_positivo(input("ID de categoría a eliminar: "))
            if not cat_id:
                print("ID inválido.")
                continue
            ok, msg = borrar_categoria(cat_id)
            print(msg)

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")