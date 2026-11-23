from peewee import DoesNotExist
from datos.modelos.noticia import Noticia


def guardar_noticia(noticia: Noticia) -> Noticia:
    noticia.save()
    return noticia


def listar_noticias(estado: str | None = None) -> list[Noticia]:
    consulta = Noticia.select().order_by(Noticia.id.desc())
    if estado:
        consulta = consulta.where(Noticia.estado == estado.strip().lower())
    return list(consulta)


def buscar_noticia_por_id(noticia_id: int) -> Noticia | None:
    try:
        return Noticia.get_by_id(noticia_id)
    except DoesNotExist:
        return None


def buscar_noticias_por_titulo(termino: str) -> list[Noticia]:
    patron = f"%{termino.strip()}%"
    return list(Noticia.select().where(Noticia.titulo ** patron).order_by(Noticia.id.desc()))


def eliminar_noticia(noticia: Noticia) -> bool:
    return noticia.delete_instance() > 0