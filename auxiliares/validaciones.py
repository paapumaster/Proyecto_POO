def texto_no_vacio(valor: str | None) -> bool:
    return isinstance(valor, str) and len(valor.strip()) > 0


def email_valido(email: str | None) -> bool:
    if not isinstance(email, str):
        return False
    correo = email.strip()
    if "@" not in correo or correo.startswith("@") or correo.endswith("@"):
        return False
    dominio = correo.split("@", 1)[1]
    return "." in dominio and not dominio.startswith(".") and not dominio.endswith(".")


def entero_positivo(valor: str | int) -> int | None:
    try:
        numero = int(str(valor).strip())
        return numero if numero > 0 else None
    except (ValueError, TypeError):
        return None


def estado_noticia_valido(estado: str | None, estados_validos: tuple[str, ...]) -> bool:
    if not isinstance(estado, str):
        return False
    return estado.strip().lower() in estados_validos