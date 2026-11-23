from auxiliares.validaciones import email_valido, texto_no_vacio
from datos.modelos.usuario import Usuario
from datos.repositorio.rol_repo import buscar_rol_por_id, listar_roles
from datos.repositorio.usuario_repo import (
    buscar_usuario_por_email,
    buscar_usuario_por_id,
    buscar_usuarios_por_nombre,
    eliminar_usuario,
    guardar_usuario,
    listar_usuarios,
)
from negocio.auth_servicio import hashear_password


def obtener_roles():
    return listar_roles()


def crear_usuario(nombre: str, email: str, password_plana: str, rol_id: int) -> tuple[bool, str]:
    if not texto_no_vacio(nombre):
        return False, "El nombre es obligatorio."
    if not email_valido(email):
        return False, "El correo electrónico no tiene un formato válido."
    if not isinstance(password_plana, str) or len(password_plana.strip()) < 4:
        return False, "La contraseña debe tener al menos 4 caracteres."
    if buscar_usuario_por_email(email):
        return False, "Ya existe un usuario registrado con ese correo."

    rol = buscar_rol_por_id(rol_id)
    if not rol:
        return False, "El rol indicado no existe."

    usuario = Usuario(
        nombre=nombre.strip(),
        email=email.strip().lower(),
        password=hashear_password(password_plana.strip()),
        rol=rol,
    )
    guardar_usuario(usuario)
    return True, f"Usuario '{usuario.nombre}' creado correctamente (ID: {usuario.id})."


def obtener_usuarios() -> list[Usuario]:
    return listar_usuarios()


def buscar_usuarios(termino: str) -> list[Usuario]:
    if not texto_no_vacio(termino):
        return []
    return buscar_usuarios_por_nombre(termino)


def actualizar_usuario(
    usuario_id: int,
    nombre: str | None = None,
    email: str | None = None,
    password_nueva: str | None = None,
    rol_id: int | None = None,
) -> tuple[bool, str]:
    usuario = buscar_usuario_por_id(usuario_id)
    if not usuario:
        return False, "Usuario no encontrado."

    if nombre is not None:
        if not texto_no_vacio(nombre):
            return False, "El nombre no puede quedar vacío."
        usuario.nombre = nombre.strip()

    if email is not None:
        if not email_valido(email):
            return False, "El correo electrónico no es válido."
        existente = buscar_usuario_por_email(email)
        if existente and existente.id != usuario.id:
            return False, "Ese correo ya está registrado en otro usuario."
        usuario.email = email.strip().lower()

    if password_nueva is not None:
        if len(password_nueva.strip()) < 4:
            return False, "La nueva contraseña debe tener al menos 4 caracteres."
        usuario.password = hashear_password(password_nueva.strip())

    if rol_id is not None:
        rol = buscar_rol_por_id(rol_id)
        if not rol:
            return False, "El rol indicado no existe."
        usuario.rol = rol

    guardar_usuario(usuario)
    return True, "Usuario actualizado correctamente."


def borrar_usuario(usuario_id: int) -> tuple[bool, str]:
    usuario = buscar_usuario_por_id(usuario_id)
    if not usuario:
        return False, "Usuario no encontrado."
    eliminar_usuario(usuario)
    return True, "Usuario eliminado correctamente."