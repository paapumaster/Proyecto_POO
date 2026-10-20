import bcrypt
from datos.plataforma_dao import PlataformaDAO
from modelos.usuario import Usuario
from modelos.noticia import Noticia

class SistemaNoticias:

    @staticmethod
    def iniciar_sesion(email, password):
        dic_usuario = PlataformaDAO.obtener_usuario_por_email(email)
        if not dic_usuario:
            return None
        
        hash_guardado = dic_usuario['password']
        
        # 1. Si la contraseña en la BD está en texto plano (ej: '1234')
        if not hash_guardado.startswith('$2'):
            if hash_guardado == password:
                return Usuario.desde_diccionario(dic_usuario)
            return None

        # 2. Si es un hash cifrado (bcrypt)
        try:
            # Adaptar formato PHP ($2y$) a Python ($2b$)
            if hash_guardado.startswith('$2y$'):
                hash_guardado = hash_guardado.replace('$2y$', '$2b$', 1)
            
            password_bytes = password.encode('utf-8')
            hash_bytes = hash_guardado.encode('utf-8')
            
            if bcrypt.checkpw(password_bytes, hash_bytes):
                return Usuario.desde_diccionario(dic_usuario)
        except Exception as e:
            # Evita que falle si algún hash de prueba tiene un salt inválido
            print(f"Aviso de formato de contraseña: {e}")
            
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
        diccionarios = PlataformaDAO.listar_noticias_por_estado('publicada')
        return [Noticia.desde_diccionario(d) for d in diccionarios]

    @staticmethod
    def obtener_noticias_en_revision():
        diccionarios = PlataformaDAO.listar_noticias_por_estado('en_revision')
        return [Noticia.desde_diccionario(d) for d in diccionarios]

    @staticmethod
    def comentar(noticia_id, lector_id, texto):
        return PlataformaDAO.agregar_comentario(noticia_id, lector_id, texto)