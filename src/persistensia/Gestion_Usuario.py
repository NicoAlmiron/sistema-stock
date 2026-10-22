from src.model.Usuario import Usuario
from src.exceptions.excepciones import DniRegistrado, AuthenticationError, ArchivoVacio
from src.utils.Helpers import verificar_clave, cabecera_menu
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


    def listar_usuarios(self, usuarios=None):
        if not usuarios:
            usuarios = self.extraer_usuarios()

        if not usuarios:
            raise ArchivoVacio('No Se Encontraron Usuarios')
        for user in usuarios:
            print(user)


    def lista_usuarios_activos(self):
        usuarios = self.extraer_usuarios()
        usuarios_activos = []
        cabecera_menu()


        for user in usuarios:
            if user.fecha_baja == "":
                usuarios_activos.append(user)

        if usuarios_activos:
            self.listar_usuarios(usuarios_activos)

            
    def lista_usuarios_suspendidos(self):
        usuarios = self.extraer_usuarios()
        usuarios_suspendidos = []
        cabecera_menu()

        for user in usuarios:
            if user.fecha_baja != "":
                usuarios_suspendidos.append(user)

        if usuarios_suspendidos:
            self.listar_usuarios(usuarios_suspendidos)
        else:
            raise ArchivoVacio('No Se Encontraron Usuarios')