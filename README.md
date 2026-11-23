# Plataforma de Noticias (PROYECTO_POO)

Aplicación de consola desarrollada en Python bajo arquitectura multicapa como continuidad de la Evaluación N°2 hacia la Evaluación N°3, incorporando ORM Peewee, autenticación con `maskpass` y `bcrypt`, y operaciones CRUD completas.

## Integrantes
- Sebastián Alfonso Durán Burgos

## Descripción general
Sistema de gestión para una plataforma de noticias conectado a MySQL (`plataforma_noticias`). Conserva los componentes previos de la Evaluación N°2 (diagramas, scripts SQL y módulos anteriores) e incorpora persistencia con Peewee (`ModelBase`), repositorios basados en funciones, capa de auxiliares, login obligatorio y CRUD desde consola para usuarios, noticias y categorías.

## Dependencias
- Python 3.10 o superior
- MySQL Server 8.x
- `peewee`
- `bcrypt`
- `maskpass`
- `pymysql`

## Procedimiento de instalación
1. Clonar el repositorio desde GitHub y abrir una terminal en la carpeta raíz del proyecto.
2. Crear y activar un entorno virtual (opcional):
   - Windows (PowerShell): `python -m venv .venv` y luego `.\.venv\Scripts\Activate.ps1`
3. Instalar las dependencias:
   - `pip install -r requirements.txt`

## Procedimiento de creación de base de datos
1. Iniciar el servidor MySQL.
2. Ejecutar o importar el script ubicado en `datos/sql/plataforma_noticias_final.sql` para crear la base de datos `plataforma_noticias` y sus tablas.
3. Ajustar, si es necesario, los parámetros de conexión en `datos/conexion.py`, `auxiliares/constantes.py` o mediante variables de entorno (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`).

## Usuario inicial
- **Correo:** `profesor@inacap.cl`
- **Contraseña:** `Profe2026*`
- En el script `datos/sql/plataforma_noticias_final.sql` también hay otros usuarios de prueba en la tabla `usuarios`. Las contraseñas con hash `bcrypt` se validan con `bcrypt.checkpw`, y si algún usuario antiguo tenía clave en texto plano al autenticarse se migra a hash `bcrypt`.

## Instrucciones de ejecución
1. Verifique que el servicio MySQL esté activo y que la base de datos `plataforma_noticias` esté creada.
2. Ejecute desde la raíz del proyecto:
   - `python main.py`
3. Ingrese sus credenciales en el login para acceder al menú principal.