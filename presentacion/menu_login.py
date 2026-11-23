import maskpass
from auxiliares.constantes import MAX_INTENTOS_LOGIN
from auxiliares.mensajes import MSG_LOGIN_EXITO, MSG_LOGIN_FALLO
from negocio.auth_servicio import autenticar_usuario


def ejecutar_login() -> dict | None:
    for intento in range(1, MAX_INTENTOS_LOGIN + 1):
        print(f"\n=== INICIO DE SESIÓN (Intento {intento}/{MAX_INTENTOS_LOGIN}) ===")
        email = input("Correo electrónico: ").strip()
        password = maskpass.askpass(prompt="Contraseña: ", mask="*")

        sesion = autenticar_usuario(email, password)
        if sesion:
            print(MSG_LOGIN_EXITO)
            print(f"Usuario: {sesion['nombre']} | Rol: {sesion['rol']}")
            return sesion

        print(MSG_LOGIN_FALLO)

    print("Se alcanzó el máximo de intentos permitidos.")
    return None