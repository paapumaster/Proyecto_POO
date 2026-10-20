class Categoria:
    def __init__(self, id, nombre, slug):
        self.id = id
        self.nombre = nombre
        self.slug = slug

    @classmethod
    def desde_diccionario(cls, dic):
        if not dic:
            return None
        return cls(
            id=dic.get('id'),
            nombre=dic.get('nombre'),
            slug=dic.get('slug')
        )