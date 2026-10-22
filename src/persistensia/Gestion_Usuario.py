from src.model.Usuario import Usuario
from src.exceptions.excepciones import DniRegistrado, AuthenticationError
from src.utils.Helpers import verificar_clave
from .Gestor_JSON import GestorJSON


class Gestion_Usuario(GestorJSON):
    def __init__(self):
        super().__init__(ruta="src/data/usuarios.json")

    def extraer_usuarios(self):
        usuarios = []
        for dicc in self.leer():
            usuarios.append(Usuario.from_dict(dicc))
        return usuarios

    def escribir_usuarios(self, usuarios):
        lista = []
        for user in usuarios:
            lista.append(user.to_dict())
        return self.guardar(lista)

    def validar_dni(self, dni):
        usuarios = self.extraer_usuarios()
        if not usuarios:
            return True
        for user in usuarios:
            if user.dni == dni:
                raise DniRegistrado(dni=dni)
        return True 

    def definir_id(self):
        usuarios = self.extraer_usuarios()
        if not usuarios:
            return 1
        return max(u.id_usuario for u in usuarios) + 1


    def registrar_usuario(self, user):

        lista_usuarios = self.extraer_usuarios()
        lista_usuarios.append(user)
        
        return self.escribir_usuarios(lista_usuarios)


    def autenticar_usuario(self, dni, clave):
        usuarios = self.extraer_usuarios()
        for user in usuarios:
            if user.dni == dni and user.validar_estado():
                if verificar_clave(clave, user.sal, user.hash):
                    return user
        raise AuthenticationError()


    def extraer_activos(self):
        activos = []
        for user in self.extraer_usuarios():
            if user.validar_estado():
                activos.append(user)
        return activos

    def extraer_suspendidos(self):
        suspendidos = []
        for user in self.extraer_usuarios():
            if not user.validar_estado():
                suspendidos.append(user)
        return suspendidos