class Usuario:
    def __init__(self, id, rol_id, nombre, email, password=None):
        self.id = id
        self.rol_id = rol_id
        self.nombre = nombre
        self.email = email
        self.password = password

    @classmethod
    def desde_diccionario(cls, dic):
        if not dic:
            return None
        return cls(
            id=dic.get('id'),
            rol_id=dic.get('rol_id'),
            nombre=dic.get('nombre'),
            email=dic.get('email'),
            password=dic.get('password')
        )