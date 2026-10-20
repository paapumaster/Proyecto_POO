from datos.plataforma_dao import PlataformaDAO
from modelos.usuario import Usuario
from modelos.noticia import Noticia

class SistemaNoticias:

    @staticmethod
    def iniciar_sesion(email, password):
        # Obtiene el diccionario del DAO
        dic_usuario = PlataformaDAO.obtener_usuario_por_email(email)
        if dic_usuario and dic_usuario['password'] == password:
            # Retorna un Objeto Usuario en lugar de un diccionario plano
            return Usuario.desde_diccionario(dic_usuario)
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
        # Convierte cada diccionario de la lista en un Objeto Noticia
        diccionarios = PlataformaDAO.listar_noticias_por_estado('publicada')
        return [Noticia.desde_diccionario(d) for d in diccionarios]

    @staticmethod
    def obtener_noticias_en_revision():
        diccionarios = PlataformaDAO.listar_noticias_por_estado('en_revision')
        return [Noticia.desde_diccionario(d) for d in diccionarios]

    @staticmethod
    def comentar(noticia_id, lector_id, texto):
        return PlataformaDAO.agregar_comentario(noticia_id, lector_id, texto)