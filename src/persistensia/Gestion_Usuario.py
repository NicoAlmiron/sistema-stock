import json
from src.model.Usuario import Usuario
from src.exceptions.excepciones import DniRegistrado, AuthenticationError, ArchivoVacio
from src.utils.Helpers import verificar_clave, cabecera_menu


class Gestion_Usuario():
    def __init__(self):
        self.arch_json = "src/data/usuarios.json"


    def extraer_usuarios(self): 
        try:
            usuarios = [] 
            with open(self.arch_json , 'r', encoding='UTF-8') as users_json:

                lista_users = json.load(users_json)
                if len(lista_users) == 0:
                    return []
                
                for user in lista_users:
                    usuario = Usuario(None,None,None,None,None,None,None).from_dict(user)
                    
                    usuarios.append(usuario)
            return usuarios
        except FileNotFoundError:
            #input("Archivo Json no encontrado!")
            return []
        except:
            return []




    def escribir_usuarios(self, usuarios):
        lista_dicc = []
        for user in usuarios:
            lista_dicc.append(user.a_dict())
        try:

            with open(self.arch_json , 'w', encoding='UTF-8') as users_json:
                arch_json = json.dumps(
                    lista_dicc,
                    indent=4)
                users_json.write(arch_json)
                return True
        except FileNotFoundError:
            with open(self.arch_json , 'w', encoding='UTF-8') as users_json:
                arch_json = json.dumps(
                    lista_dicc,
                    indent=4)
                users_json.write(arch_json)
                return True
        except FileExistsError:
            input("A sucedido un error inesperado!")
            return False

    
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


    def registrar_usuario(self):

        lista_usuarios = self.extraer_usuarios()
        lista_usuarios.append(self)
        
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
            raise ArchivoVacio('|· No Se Encontraron Usuarios')
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
            raise ArchivoVacio('|· No Se Encontraron Usuarios')

    