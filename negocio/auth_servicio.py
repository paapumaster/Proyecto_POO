import bcrypt
from datos.repositorio.usuario_repo import buscar_usuario_por_email, guardar_usuario


def es_hash_bcrypt(valor: str | None) -> bool:
    if not isinstance(valor, str):
        return False
    return valor.startswith(("$2a$", "$2b$", "$2y$"))


def hashear_password(password_plana: str) -> str:
    return bcrypt.hashpw(password_plana.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_password(password_plana: str, password_guardada: str) -> bool:
    if not password_plana or not password_guardada:
        return False
    if es_hash_bcrypt(password_guardada):
        try:
            return bcrypt.checkpw(
                password_plana.encode("utf-8"),
                password_guardada.encode("utf-8"),
            )
        except ValueError:
            return False
    return password_plana.strip() == password_guardada.strip()


def autenticar_usuario(email: str, password_plana: str) -> dict | None:
    if not email or not password_plana:
        return None
    usuario = buscar_usuario_por_email(email)
    if not usuario:
        return None
    if not verificar_password(password_plana, usuario.password):
        return None

    # Si venía en texto plano desde la BD anterior, se actualiza automáticamente a hash bcrypt
    if not es_hash_bcrypt(usuario.password):
        usuario.password = hashear_password(password_plana.strip())
        guardar_usuario(usuario)

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rol": usuario.rol.nombre,
    }