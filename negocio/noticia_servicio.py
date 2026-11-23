from datetime import datetime
from auxiliares.constantes import ESTADOS_NOTICIA
from auxiliares.validaciones import estado_noticia_valido, texto_no_vacio
from datos.modelos.noticia import Noticia
from datos.repositorio.noticia_repo import (
    buscar_noticia_por_id,
    buscar_noticias_por_titulo,
    eliminar_noticia,
    guardar_noticia,
    listar_noticias,
)


def crear_noticia(titulo: str, contenido: str, estado: str = "borrador") -> tuple[bool, str]:
    if not texto_no_vacio(titulo) or not texto_no_vacio(contenido):
        return False, "El título y el contenido de la noticia son obligatorios."

    estado_limpio = estado.strip().lower()
    if not estado_noticia_valido(estado_limpio, ESTADOS_NOTICIA):
        return False, f"Estado inválido. Estados permitidos: {', '.join(ESTADOS_NOTICIA)}."

    fecha_pub = datetime.now() if estado_limpio == "publicada" else None
    noticia = Noticia(
        titulo=titulo.strip(),
        contenido=contenido.strip(),
        estado=estado_limpio,
        fecha_publicacion=fecha_pub,
    )
    guardar_noticia(noticia)
    return True, f"Noticia '{noticia.titulo}' creada correctamente (ID: {noticia.id})."


def obtener_noticias(estado: str | None = None) -> list[Noticia]:
    return listar_noticias(estado)


def buscar_noticias(termino: str) -> list[Noticia]:
    if not texto_no_vacio(termino):
        return []
    return buscar_noticias_por_titulo(termino)


def actualizar_noticia(
    noticia_id: int,
    titulo: str | None = None,
    contenido: str | None = None,
    estado: str | None = None,
) -> tuple[bool, str]:
    noticia = buscar_noticia_por_id(noticia_id)
    if not noticia:
        return False, "Noticia no encontrada."

    if titulo is not None:
        if not texto_no_vacio(titulo):
            return False, "El título no puede quedar vacío."
        noticia.titulo = titulo.strip()

    if contenido is not None:
        if not texto_no_vacio(contenido):
            return False, "El contenido no puede quedar vacío."
        noticia.contenido = contenido.strip()

    if estado is not None:
        estado_limpio = estado.strip().lower()
        if not estado_noticia_valido(estado_limpio, ESTADOS_NOTICIA):
            return False, f"Estado inválido. Estados permitidos: {', '.join(ESTADOS_NOTICIA)}."
        noticia.estado = estado_limpio
        if estado_limpio == "publicada" and not noticia.fecha_publicacion:
            noticia.fecha_publicacion = datetime.now()

    guardar_noticia(noticia)
    return True, "Noticia actualizada correctamente."


def borrar_noticia(noticia_id: int) -> tuple[bool, str]:
    noticia = buscar_noticia_por_id(noticia_id)
    if not noticia:
        return False, "Noticia no encontrada."
    eliminar_noticia(noticia)
    return True, "Noticia eliminada correctamente."