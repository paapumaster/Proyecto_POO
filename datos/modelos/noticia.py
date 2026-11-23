from datetime import datetime
from peewee import AutoField, CharField, DateTimeField, TextField
from datos.modelos.base import ModelBase


class Noticia(ModelBase):
    id = AutoField()
    titulo = CharField(max_length=255)
    contenido = TextField()
    estado = CharField(max_length=20, default="borrador")
    fecha_creacion = DateTimeField(default=datetime.now)
    fecha_publicacion = DateTimeField(null=True)

    class Meta:
        table_name = "noticias"