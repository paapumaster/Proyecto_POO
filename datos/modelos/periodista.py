from peewee import AutoField, CharField, ForeignKeyField
from datos.modelos.base import ModelBase
from datos.modelos.usuario import Usuario


class Periodista(ModelBase):
    id = AutoField()
    usuario = ForeignKeyField(
        Usuario,
        column_name="usuario_id",
        backref="perfiles_periodista",
        on_delete="CASCADE",
        on_update="CASCADE",
        null=True,
    )
    nombre = CharField(max_length=100)
    especialidad = CharField(max_length=100, default="General")

    class Meta:
        table_name = "periodistas"