class Noticia:
    def __init__(self, id, titulo, contenido, estado, fecha_creacion=None, fecha_publicacion=None):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.fecha_publicacion = fecha_publicacion

    @classmethod
    def desde_diccionario(cls, dic):
        if not dic:
            return None
        return cls(
            id=dic.get('id'),
            titulo=dic.get('titulo'),
            contenido=dic.get('contenido'),
            estado=dic.get('estado'),
            fecha_creacion=dic.get('fecha_creacion'),
            fecha_publicacion=dic.get('fecha_publicacion')
        )