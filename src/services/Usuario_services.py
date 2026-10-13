from src.persistensia.Usuario_JSON import extraer_usuarios, escribir_usuarios
from src.exceptions.excepciones import DatoNumericoObligatorio, AuthenticationError
from src.exceptions.excepciones import DniRegistrado
from src.utils.Helpers import verificar_clave

# Registro de usuario 

def validar_dni(dni):
    usuarios = extraer_usuarios()
    if not usuarios:
        return True
    for user in usuarios:
        if user.dni == dni:
            raise DniRegistrado()
    return True

def pedir_dni():
    while True:
        dni = input('|#-DNI: ')
        if not dni.isdigit():
            input("|· El DNI tiene que ser valido!")
        else:
            if validar_dni(dni):
                return dni
    
def definir_id():
    usuarios = extraer_usuarios()
    if not usuarios:
        return 1
    return max(u.id_usuario for u in usuarios) + 1

def registrar_usuario(usuario):

    lista_usuarios = extraer_usuarios()
    lista_usuarios.append(usuario)
    
    return escribir_usuarios(lista_usuarios)

#Logeo

def autenticar_usuario(dni, clave):
    usuarios = extraer_usuarios()
    for user in usuarios:
        if user.dni == dni:
            if verificar_clave(clave, user.sal, user.hash):
                return user
    raise AuthenticationError()

def verificar_permisos(user):
    if user.rol == "ADMINISTRADOR":
        return True
    elif user.rol == "EMPLEADO":
        return False



def listar_usuarios(usuarios=None) -> None:
    if not usuarios:
        usuarios = extraer_usuarios()
    for user in usuarios:
        print(user)

def lista_usuarios_activos():
    usuarios = extraer_usuarios()
    usuarios_activos = []

    for user in usuarios:
        if user.fecha_baja is "":
            usuarios_activos.append(user)

    return usuarios_activos

def lista_usuarios_suspendidos():
    usuarios = extraer_usuarios()
    usuarios_suspendidos = []

    for user in usuarios:
        if user.fecha_baja is not "":
            usuarios_suspendidos.append(user)

    return usuarios_suspendidos