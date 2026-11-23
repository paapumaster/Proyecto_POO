from auxiliares.validaciones import texto_no_vacio
from datos.modelos.categoria import Categoria
from datos.repositorio.categoria_repo import (
    buscar_categoria_por_id,
    buscar_categoria_por_nombre,
    eliminar_categoria,
    guardar_categoria,
    listar_categorias,
)


def _crear_slug(texto: str) -> str:
    base = texto.strip().lower().replace(" ", "-")
    return "".join(c for c in base if c.isalnum() or c == "-")


def crear_categoria(nombre: str, slug: str | None = None) -> tuple[bool, str]:
    if not texto_no_vacio(nombre):
        return False, "El nombre de la categoría es obligatorio."

    slug_final = _crear_slug(slug) if slug and texto_no_vacio(slug) else _crear_slug(nombre)
    if not slug_final:
        return False, "No se pudo generar un slug válido."

    if buscar_categoria_por_nombre(nombre):
        return False, "Ya existe una categoría con ese nombre."

    categoria = Categoria(nombre=nombre.strip(), slug=slug_final)
    guardar_categoria(categoria)
    return True, f"Categoría '{categoria.nombre}' creada correctamente (ID: {categoria.id})."


def obtener_categorias() -> list[Categoria]:
    return listar_categorias()


def buscar_categoria(categoria_id: int) -> Categoria | None:
    return buscar_categoria_por_id(categoria_id)


def actualizar_categoria(
    categoria_id: int,
    nombre: str | None = None,
    slug: str | None = None,
) -> tuple[bool, str]:
    categoria = buscar_categoria_por_id(categoria_id)
    if not categoria:
        return False, "Categoría no encontrada."

    if nombre is not None:
        if not texto_no_vacio(nombre):
            return False, "El nombre no puede quedar vacío."
        categoria.nombre = nombre.strip()
        if slug is None:
            categoria.slug = _crear_slug(nombre)

    if slug is not None:
        slug_limpio = _crear_slug(slug)
        if not slug_limpio:
            return False, "El slug no es válido."
        categoria.slug = slug_limpio

    guardar_categoria(categoria)
    return True, "Categoría actualizada correctamente."


def borrar_categoria(categoria_id: int) -> tuple[bool, str]:
    categoria = buscar_categoria_por_id(categoria_id)
    if not categoria:
        return False, "Categoría no encontrada."
    eliminar_categoria(categoria)
    return True, "Categoría eliminada correctamente."