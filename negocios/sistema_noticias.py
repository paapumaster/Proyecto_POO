from datos.plataforma_dao import PlataformaDAO

class SistemaNoticias:

    @staticmethod
    def iniciar_sesion(email, password):
        usuario = PlataformaDAO.obtener_usuario_por_email(email)
        if usuario and usuario['password'] == password:
            return usuario
        return None

    @staticmethod
    def crear_noticia_borrador(titulo, contenido, periodista_id):
        return PlataformaDAO.registrar_noticia(titulo, contenido, periodista_id)

    @staticmethod
    def enviar_a_revision(noticia_id):
        return PlataformaDAO.cambiar_estado_noticia(noticia_id, 'en_revision')

    @staticmethod
    def publicar_noticia(noticia_id):
        return PlataformaDAO.cambiar_estado_noticia(noticia_id, 'publicada')

    @staticmethod
    def obtener_noticias_publicadas():
        return PlataformaDAO.listar_noticias_por_estado('publicada')

    @staticmethod
    def obtener_noticias_en_revision():
        return PlataformaDAO.listar_noticias_por_estado('en_revision')

    @staticmethod
    def comentar(noticia_id, lector_id, texto):
        return PlataformaDAO.agregar_comentario(noticia_id, lector_id, texto)