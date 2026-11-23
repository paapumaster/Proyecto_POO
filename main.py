from auxiliares.mensajes import MSG_SIN_ACCESO
from datos.conexion import cerrar_bd, conectar_bd, db
from datos.modelos import (
    Categoria,
    Comentario,
    Noticia,
    NoticiaAutor,
    NoticiaCategoria,
    NoticiaEtiqueta,
    NoticiaGuardada,
    Periodista,
    Rol,
    Usuario,
)
from presentacion.menu_login import ejecutar_login
from presentacion.menu_principal import mostrar_menu_principal


def inicializar_tablas() -> None:
    db.create_tables(
        [
            Rol,
            Usuario,
            Periodista,
            Categoria,
            Noticia,
            Comentario,
            NoticiaAutor,
            NoticiaCategoria,
            NoticiaEtiqueta,
            NoticiaGuardada,
        ],
        safe=True,
    )


def main() -> None:
    conectar_bd()
    try:
        inicializar_tablas()
        sesion = ejecutar_login()
        if not sesion:
            print(MSG_SIN_ACCESO)
            return
        mostrar_menu_principal(sesion)
    finally:
        cerrar_bd()


if __name__ == "__main__":
    main()