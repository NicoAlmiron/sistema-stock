from src.persistensia.Gestion_Usuario import Gestion_Usuario
from src.model.Usuario import Usuario
from src.exceptions.excepciones import (DniRegistrado, OperacionCancelada, TecStoreError,
                                        DatoNumericoObligatorio, NumeroDemasiadoAlto, TecStoreError)
from src.utils.Helpers import (limpiar_consola, cabecera_menu, pedir_nombre, pedir_id, pedir_telefono,
                               definir_clave, definir_rol, hashear_clave, guion_titulo, guion_item, 
                               guion_sub_item, pausar_consola)



def pedir_dni():
    while True:
        dni = input(f'|{" "*20}#-DNI: ')
        if dni == "":
            raise OperacionCancelada()
        elif not dni.isdigit():
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
            guion_titulo('REGISTRO DE USUARIO NUEVOS')
            id_usuario = Gestion_Usuario().definir_id()
            nombre = pedir_nombre(input(f'|{" "*20}#-NOMBRE: '))
            dni = pedir_dni()            
            telefono = pedir_telefono()
            rol = definir_rol()
            clave = definir_clave()

            sal = None
            hash = None
            sal, hash = hashear_clave(clave)

            usuario = Usuario(id_usuario, nombre, dni, telefono, rol, sal, hash)

            if Gestion_Usuario().registrar_usuario(usuario):
                pausar_consola("Usuario registrado con exito!")
                return
            else:
                raise TecStoreError()
            
        except TecStoreError as e:
            pausar_consola(e.mensaje)
            break



def suspender_usuario():
    usuarios = Gestion_Usuario().extraer_usuarios()
    sin_coincidencias = False
    try:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('SUSPENCION DE USUARIOS')
        Gestion_Usuario().listar_usuarios()
        guion_item('Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))
            
        for user in usuarios:
            if user.id_usuario == id_buscar and user.rol != "ADMINISTRADOR":
                sin_coincidencias = True
                limpiar_consola()
                cabecera_menu()
                print(user)
                guion_sub_item(f" *Esta seguro que quiere suspender este Usuario?")
                guion_sub_item('  *Para confirmar, ingrese el DNI del usuario')
                dni = pedir_dni()  

                if Gestion_Usuario().validar_dni(dni) is True:
                    raise OperacionCancelada()

        if sin_coincidencias is False:
            pausar_consola('No se encontro el usuario')
                
    except DniRegistrado as er_dni: 
                if user.dni == er_dni.dni:
                    user.baja_usuario()
                    Gestion_Usuario().escribir_usuarios(usuarios)
                    pausar_consola("Se Suspendio el usuario exitosamente!")
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        pausar_consola(er.mensaje_default)
    except ValueError:
        pausar_consola('Ingrese valores Numericos')

def reactivar_usuario():
    usuarios = Gestion_Usuario().extraer_usuarios()
    sin_coincidencias = False
    dni = None
    try:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('REACTIVACION DE USUARIOS')
        Gestion_Usuario().lista_usuarios_suspendidos()
        guion_item('Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))
            
        for user in usuarios:
            if user.id_usuario == id_buscar and user.fecha_baja is not "":
                sin_coincidencias = True
                limpiar_consola()
                cabecera_menu()
                print(user)
                guion_sub_item(f" *Esta seguro que quiere Reactivar este Usuario?")
                guion_sub_item( ' *Para confirmar, ingrese el DNI del usuario')
                dni = pedir_dni()  

                if Gestion_Usuario().validar_dni(dni) is True:
                    raise OperacionCancelada()

        if sin_coincidencias is False:
            pausar_consola('No se encontro el usuario')
    except DniRegistrado as error_dni: 
                if user.dni == error_dni.dni:
                    user.reactivacion_usuario()
                    Gestion_Usuario().escribir_usuarios(usuarios)
                    pausar_consola("Se Reactivo el usuario exitosamente!")
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        pausar_consola(er.mensaje_default)
    except ValueError:
        pausar_consola('Ingrese valores Numericos')











