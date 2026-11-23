from datetime import datetime
from peewee import DateTimeField, ForeignKeyField
from datos.modelos.base import ModelBase
from datos.modelos.categoria import Categoria
from datos.modelos.noticia import Noticia
from datos.modelos.usuario import Usuario


class NoticiaAutor(ModelBase):
    noticia = ForeignKeyField(
        Noticia,
        column_name="noticia_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    usuario = ForeignKeyField(
        Usuario,
        column_name="usuario_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )

    class Meta:
        table_name = "noticia_autores"
        primary_key = False


class NoticiaCategoria(ModelBase):
    noticia = ForeignKeyField(
        Noticia,
        column_name="noticia_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    categoria = ForeignKeyField(
        Categoria,
        column_name="categoria_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )

    class Meta:
        table_name = "noticia_categorias"
        primary_key = False


class NoticiaEtiqueta(ModelBase):
    noticia = ForeignKeyField(
        Noticia,
        column_name="noticia_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    etiqueta_id = ForeignKeyField(
        ModelBase,
        column_name="etiqueta_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )

    class Meta:
        table_name = "noticia_etiquetas"
        primary_key = False


class NoticiaGuardada(ModelBase):
    usuario = ForeignKeyField(
        Usuario,
        column_name="usuario_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    noticia = ForeignKeyField(
        Noticia,
        column_name="noticia_id",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    fecha_guardado = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "noticias_guardadas"
        primary_key = False