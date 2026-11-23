from auxiliares.validaciones import entero_positivo
from negocio.usuario_servicio import (
    actualizar_usuario,
    borrar_usuario,
    buscar_usuarios,
    crear_usuario,
    obtener_roles,
    obtener_usuarios,
)


def menu_gestion_usuarios() -> None:
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por nombre")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("0. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            roles = obtener_roles()
            if roles:
                print("Roles disponibles:", ", ".join(f"{r.id}: {r.nombre}" for r in roles))
            nombre = input("Nombre: ")
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            rol_id = entero_positivo(input("ID de Rol: "))
            if not rol_id:
                print("Debe ingresar un ID de rol válido.")
                continue
            ok, msg = crear_usuario(nombre, email, password, rol_id)
            print(msg)

        elif opcion == "2":
            usuarios = obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
                continue
            print("\nID | Nombre | Email | Rol")
            for u in usuarios:
                print(f"{u.id} | {u.nombre} | {u.email} | {u.rol.nombre}")

        elif opcion == "3":
            termino = input("Nombre o parte del nombre a buscar: ")
            encontrados = buscar_usuarios(termino)
            if not encontrados:
                print("No se encontraron usuarios con ese criterio.")
                continue
            for u in encontrados:
                print(f"[{u.id}] {u.nombre} ({u.email}) - Rol: {u.rol.nombre}")

        elif opcion == "4":
            usuario_id = entero_positivo(input("ID del usuario a modificar: "))
            if not usuario_id:
                print("ID inválido.")
                continue
            nombre_txt = input("Nuevo nombre (Enter para no cambiar): ").strip()
            email_txt = input("Nuevo email (Enter para no cambiar): ").strip()
            pass_txt = input("Nueva contraseña (Enter para no cambiar): ").strip()
            rol_txt = input("Nuevo ID de rol (Enter para no cambiar): ").strip()

            nombre = nombre_txt if nombre_txt else None
            email = email_txt if email_txt else None
            password = pass_txt if pass_txt else None
            rol_id = entero_positivo(rol_txt) if rol_txt else None

            ok, msg = actualizar_usuario(usuario_id, nombre, email, password, rol_id)
            print(msg)

        elif opcion == "5":
            usuario_id = entero_positivo(input("ID del usuario a eliminar: "))
            if not usuario_id:
                print("ID inválido.")
                continue
            ok, msg = borrar_usuario(usuario_id)
            print(msg)

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")