from src.persistensia.Usuario_JSON import extraer_usuarios, escribir_usuarios
from src.exceptions.excepciones import DatoNumericoObligatorio, AuthenticationError, NumeroDemasiadoAlto, NumeroNegativoError
from src.exceptions.excepciones import DniRegistrado, ArchivoVacio, TecStoreError, OperacionCancelada
from src.utils.Helpers import verificar_clave, cabecera_menu, pedir_id, limpiar_consola
from datetime import datetime

# Registro de usuario 

def validar_dni(dni):
    usuarios = extraer_usuarios()
    if not usuarios:
        return True
    for user in usuarios:
        if user.dni == dni:
            raise DniRegistrado(dni=dni)
    return True

def pedir_dni():
    while True:
        dni = input('|#-DNI: ')
        if not dni.isdigit():
            raise DatoNumericoObligatorio()
        elif len(dni) > 10:
            raise NumeroDemasiadoAlto()
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
        if user.dni == dni and user.validar_estado():
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

    if not usuarios:
        raise ArchivoVacio('|· No Se Encontraron Usuarios')
    for user in usuarios:
        print(user)

def lista_usuarios_activos():
    usuarios = extraer_usuarios()
    usuarios_activos = []
    cabecera_menu()


    for user in usuarios:
        if user.fecha_baja == "":
            usuarios_activos.append(user)

    if usuarios_activos:
        listar_usuarios(usuarios_activos)

def lista_usuarios_suspendidos():
    usuarios = extraer_usuarios()
    usuarios_suspendidos = []
    cabecera_menu()

    for user in usuarios:
        if user.fecha_baja != "":
            usuarios_suspendidos.append(user)

    if usuarios_suspendidos:
        listar_usuarios(usuarios_suspendidos)
    else:
        raise ArchivoVacio('|· No Se Encontraron Usuarios')


def suspender_usuario():
    usuarios = extraer_usuarios()
    sin_coincidencias = False
    usuario = None
    try:
        cabecera_menu()
        listar_usuarios()
        print('|##-· Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))
        
        for user in usuarios:
            if user.id_usuario == id_buscar and user.rol != "ADMINISTRADOR":
                usuario = user
                sin_coincidencias = True
                limpiar_consola()
                cabecera_menu()
                print(user)
                print(f"# *Esta seguro que quiere suspender este Usuario?")
                print( '#  *Para confirmar, ingrese el DNI del usuario')
                dni = pedir_dni()  

                if validar_dni(dni) is True:
                    raise OperacionCancelada()

        if sin_coincidencias is False:
            print('|· No se encontro el usuario')
            
    except DniRegistrado as er_dni: 
                if user.dni == er_dni.dni:
                    user.fecha_baja = datetime.now()
                    escribir_usuarios(usuarios)
                    print("Se Suspendio el usuario exitosamente!")
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        input(er)
    except ValueError:
        input('|· Ingrese valores Numericos')


def reactivar_usuario():
    usuarios = extraer_usuarios()
    sin_coincidencias = False
    dni = None
    try:
        lista_usuarios_suspendidos()
        print('|##-· Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))
        
        for user in usuarios:
            if user.id_usuario == id_buscar and user.fecha_baja is not "":
                sin_coincidencias = True
                limpiar_consola()
                cabecera_menu()
                print(user)
                print(f"# *Esta seguro que quiere Reactivar este Usuario?")
                print( '#  *Para confirmar, ingrese el DNI del usuario')
                dni = pedir_dni()  

                if validar_dni(dni) is True:
                    raise OperacionCancelada()

        if sin_coincidencias is False:
            print('|· No se encontro el usuario')
    except DniRegistrado as error_dni: 
                if user.dni == error_dni.dni:
                    user.fecha_baja = ""
                    escribir_usuarios(usuarios)
                    print("Se Reactivo el usuario exitosamente!")
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        input(er)
    except ValueError:
        input('|· Ingrese valores Numericos')