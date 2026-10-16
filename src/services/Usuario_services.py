from src.persistensia.Gestion_Usuario import Gestion_Usuario
from src.model.Usuario import Usuario
from src.exceptions.excepciones import DniRegistrado, OperacionCancelada, TecStoreError
from src.exceptions.excepciones import DatoNumericoObligatorio, NumeroDemasiadoAlto, TecStoreError
from src.utils.Helpers import limpiar_consola, cabecera_menu, pedir_nombre, pedir_id, pedir_telefono
from src.utils.Helpers import definir_clave, definir_rol, hashear_clave
#from src.services.Actividad_services import Login



def pedir_dni():
    while True:
        dni = input('|#-DNI: ')
        if not dni.isdigit():
            raise DatoNumericoObligatorio()
        elif len(dni) > 10:
            raise NumeroDemasiadoAlto()
        else:
            if Gestion_Usuario().validar_dni(dni):
                return dni


def registrar_usuario():
    while True:
        try:
            limpiar_consola()
            cabecera_menu()
            print('|##··REGISTROS DE DATOS··##|')
            id_usuario = Gestion_Usuario().definir_id()
            nombre = pedir_nombre(input('|#-NOMBRE: '))
            dni = pedir_dni()            
            telefono = pedir_telefono()
            rol = definir_rol()
            clave = definir_clave()

            sal = None
            hash = None
            sal, hash = hashear_clave(clave)

            usuario = Usuario(id_usuario, nombre, dni, telefono, rol, sal, hash)

            if registrar_usuario(usuario):
                print("|· Usuario registrado con exito!")
                return
            else:
                raise TecStoreError()
            
        except TecStoreError as e:
            input(e)
            break



def suspender_usuario():
    usuarios = Gestion_Usuario().extraer_usuarios()
    sin_coincidencias = False
    try:
        cabecera_menu()
        Gestion_Usuario().listar_usuarios()
        print('|##-· Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))
            
        for user in usuarios:
            if user.id_usuario == id_buscar and user.rol != "ADMINISTRADOR":
                #usuario = user
                sin_coincidencias = True
                limpiar_consola()
                cabecera_menu()
                print(user)
                print(f"# *Esta seguro que quiere suspender este Usuario?")
                print( '#  *Para confirmar, ingrese el DNI del usuario')
                dni = pedir_dni()  

                if Gestion_Usuario().validar_dni(dni) is True:
                    raise OperacionCancelada()

        if sin_coincidencias is False:
            print('|· No se encontro el usuario')
                
    except DniRegistrado as er_dni: 
                if user.dni == er_dni.dni:
                    user.baja_usuario()
                    Gestion_Usuario().escribir_usuarios(usuarios)
                    print("Se Suspendio el usuario exitosamente!")
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        input(er)
    except ValueError:
        input('|· Ingrese valores Numericos')

def reactivar_usuario():
    usuarios = Gestion_Usuario().extraer_usuarios()
    sin_coincidencias = False
    dni = None
    try:
        Gestion_Usuario().lista_usuarios_suspendidos()
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

                if Gestion_Usuario().validar_dni(dni) is True:
                    raise OperacionCancelada()

        if sin_coincidencias is False:
            print('|· No se encontro el usuario')
    except DniRegistrado as error_dni: 
                if user.dni == error_dni.dni:
                    user.reactivacion_usuario()
                    Gestion_Usuario().escribir_usuarios(usuarios)
                    print("Se Reactivo el usuario exitosamente!")
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        input(er)
    except ValueError:
        input('|· Ingrese valores Numericos')











