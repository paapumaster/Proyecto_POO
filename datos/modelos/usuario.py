from datetime import datetime
from peewee import AutoField, CharField, DateTimeField, ForeignKeyField
from datos.modelos.base import ModelBase
from datos.modelos.rol import Rol


class Usuario(ModelBase):
    id = AutoField()
    rol = ForeignKeyField(
        Rol,
        column_name="rol_id",
        backref="usuarios",
        on_delete="RESTRICT",
        on_update="CASCADE",
    )
    nombre = CharField(max_length=100)
    email = CharField(max_length=150, unique=True)
    password = CharField(max_length=255)
    fecha_registro = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "usuarios"