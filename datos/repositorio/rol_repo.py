from peewee import DoesNotExist
from datos.modelos.rol import Rol


def guardar_rol(rol: Rol) -> Rol:
    rol.save()
    return rol


def listar_roles() -> list[Rol]:
    return list(Rol.select().order_by(Rol.id))


def buscar_rol_por_id(rol_id: int) -> Rol | None:
    try:
        return Rol.get_by_id(rol_id)
    except DoesNotExist:
        return None


def buscar_rol_por_nombre(nombre: str) -> Rol | None:
    try:
        return Rol.get(Rol.nombre ** nombre.strip())
    except DoesNotExist:
        return None