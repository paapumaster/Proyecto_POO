DB_NAME = "plataforma_noticias"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = ""

MAX_INTENTOS_LOGIN = 3

ESTADOS_NOTICIA = (
    "borrador",
    "en_revision",
    "publicada",
    "rechazada",
    "archivada",
)

TIPOS_RECURSO = (
    "imagen",
    "video",
    "documento",
    "audio",
)

ROL_ADMIN = "Administrador"
ROL_EDITOR = "Editor"
ROL_PERIODISTA = "Periodista"
ROL_LECTOR = "Lector"