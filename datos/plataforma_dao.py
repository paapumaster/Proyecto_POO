from datos.conexion import obtener_conexion

class PlataformaDAO:

    @staticmethod
    def obtener_usuario_por_email(email):
        conexion = obtener_conexion()
        if not conexion:
            return None
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT id, rol_id, nombre, email, password FROM usuarios WHERE email = %s"
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()
            return usuario
        finally:
            conexion.close()

    @staticmethod
    def registrar_noticia(titulo, contenido, autor_id):
        conexion = obtener_conexion()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            # Se crea la noticia por defecto en estado 'borrador'
            sql_noticia = "INSERT INTO noticias (titulo, contenido, estado) VALUES (%s, %s, 'borrador')"
            cursor.execute(sql_noticia, (titulo, contenido))
            noticia_id = cursor.lastrowid

            # Asociar el periodista/autor en noticia_autores
            sql_autor = "INSERT INTO noticia_autores (noticia_id, usuario_id) VALUES (%s, %s)"
            cursor.execute(sql_autor, (noticia_id, autor_id))

            conexion.commit()
            return noticia_id
        except Exception as e:
            conexion.rollback()
            print(f"Error al registrar noticia: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def cambiar_estado_noticia(noticia_id, nuevo_estado):
        conexion = obtener_conexion()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            if nuevo_estado == 'publicada':
                sql = "UPDATE noticias SET estado = %s, fecha_publicacion = NOW() WHERE id = %s"
            else:
                sql = "UPDATE noticias SET estado = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_estado, noticia_id))
            conexion.commit()
            return cursor.rowcount > 0
        finally:
            conexion.close()

    @staticmethod
    def listar_noticias_por_estado(estado):
        conexion = obtener_conexion()
        if not conexion:
            return []
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT n.id, n.titulo, n.contenido, n.estado, n.fecha_creacion, n.fecha_publicacion
                FROM noticias n
                WHERE n.estado = %s
                ORDER BY n.fecha_creacion DESC
            """
            cursor.execute(sql, (estado,))
            return cursor.fetchall()
        finally:
            conexion.close()

    @staticmethod
    def agregar_comentario(noticia_id, usuario_id, comentario):
        conexion = obtener_conexion()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO comentarios (noticia_id, usuario_id, comentario) VALUES (%s, %s, %s)"
            cursor.execute(sql, (noticia_id, usuario_id, comentario))
            conexion.commit()
            return True
        finally:
            conexion.close()