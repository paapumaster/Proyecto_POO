import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    """
    Retorna un objeto de conexión a la base de datos MySQL.
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='sebamaster',
            password='seba123',
            database='plataforma_noticias'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None