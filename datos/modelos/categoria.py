from peewee import AutoField, CharField
from datos.modelos.base import ModelBase


class Categoria(ModelBase):
    id = AutoField()
    nombre = CharField(max_length=100, unique=True)
    slug = CharField(max_length=120, unique=True)

    class Meta:
        table_name = "categorias"