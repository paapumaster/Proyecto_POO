from peewee import AutoField, CharField
from datos.modelos.base import ModelBase


class Rol(ModelBase):
    id = AutoField()
    nombre = CharField(max_length=50, unique=True)

    class Meta:
        table_name = "roles"