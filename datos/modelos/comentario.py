from datetime import datetime
from peewee import AutoField, DateTimeField, ForeignKeyField, TextField
from datos.modelos.base import ModelBase
from datos.modelos.noticia import Noticia
from datos.modelos.usuario import Usuario


class Comentario(ModelBase):
    id = AutoField()
    noticia = ForeignKeyField(
        Noticia,
        column_name="noticia_id",
        backref="comentarios",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    usuario = ForeignKeyField(
        Usuario,
        column_name="usuario_id",
        backref="comentarios",
        on_delete="CASCADE",
        on_update="CASCADE",
    )
    comentario = TextField()
    fecha = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "comentarios"