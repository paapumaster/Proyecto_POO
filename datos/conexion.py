import os
from peewee import MySQLDatabase
from auxiliares.constantes import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
)

db = MySQLDatabase(
    os.getenv("DB_NAME", DB_NAME),
    host=os.getenv("DB_HOST", DB_HOST),
    port=int(os.getenv("DB_PORT", DB_PORT)),
    user=os.getenv("DB_USER", DB_USER),
    password=os.getenv("DB_PASSWORD", DB_PASSWORD),
    charset="utf8mb4",
)


def conectar_bd() -> None:
    if db.is_closed():
        db.connect(reuse_if_open=True)


def cerrar_bd() -> None:
    if not db.is_closed():
        db.close()