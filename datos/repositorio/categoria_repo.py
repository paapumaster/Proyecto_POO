from peewee import DoesNotExist
from datos.modelos.categoria import Categoria


def guardar_categoria(categoria: Categoria) -> Categoria:
    categoria.save()
    return categoria


def listar_categorias() -> list[Categoria]:
    return list(Categoria.select().order_by(Categoria.id))


def buscar_categoria_por_id(categoria_id: int) -> Categoria | None:
    try:
        return Categoria.get_by_id(categoria_id)
    except DoesNotExist:
        return None


def buscar_categoria_por_nombre(nombre: str) -> Categoria | None:
    try:
        return Categoria.get(Categoria.nombre ** nombre.strip())
    except DoesNotExist:
        return None


def eliminar_categoria(categoria: Categoria) -> bool:
    return categoria.delete_instance() > 0