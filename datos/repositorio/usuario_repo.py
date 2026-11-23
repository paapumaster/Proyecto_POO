from peewee import DoesNotExist
from datos.modelos.usuario import Usuario


def guardar_usuario(usuario: Usuario) -> Usuario:
    usuario.save()
    return usuario


def listar_usuarios() -> list[Usuario]:
    return list(Usuario.select().order_by(Usuario.id))


def buscar_usuario_por_id(usuario_id: int) -> Usuario | None:
    try:
        return Usuario.get_by_id(usuario_id)
    except DoesNotExist:
        return None


def buscar_usuario_por_email(email: str) -> Usuario | None:
    try:
        return Usuario.get(Usuario.email == email.strip().lower())
    except DoesNotExist:
        return None


def buscar_usuarios_por_nombre(termino: str) -> list[Usuario]:
    patron = f"%{termino.strip()}%"
    return list(Usuario.select().where(Usuario.nombre ** patron).order_by(Usuario.id))


def eliminar_usuario(usuario: Usuario) -> bool:
    return usuario.delete_instance() > 0