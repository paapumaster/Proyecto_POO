from peewee import DoesNotExist
from datos.modelos.periodista import Periodista
from datos.modelos.rol import Rol
from datos.modelos.usuario import Usuario


def guardar_periodista(periodista: Periodista) -> Periodista:
    periodista.save()
    return periodista


def listar_periodistas() -> list[Periodista]:
    return list(Periodista.select().order_by(Periodista.id))


def buscar_periodista_por_id(periodista_id: int) -> Periodista | None:
    try:
        return Periodista.get_by_id(periodista_id)
    except DoesNotExist:
        return None


def buscar_periodistas_por_especialidad(especialidad: str) -> list[Periodista]:
    patron = f"%{especialidad.strip()}%"
    return list(Periodista.select().where(Periodista.especialidad ** patron).order_by(Periodista.id))


def listar_usuarios_periodistas() -> list[Usuario]:
    rol_per = Rol.get_or_none(Rol.nombre == "Periodista")
    if not rol_per:
        return []
    return list(Usuario.select().where(Usuario.rol == rol_per).order_by(Usuario.id))


def eliminar_periodista(periodista: Periodista) -> bool:
    return periodista.delete_instance() > 0