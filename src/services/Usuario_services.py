from src.persistensia.Gestion_Usuario import Gestion_Usuario
from src.model.Usuario import Usuario
from src.exceptions.excepciones import (OperacionCancelada, TecStoreError, IdNoEncontrado,
                                        DatoNumericoObligatorio, NumeroDemasiadoAlto, ArchivoVacio)
from src.utils.Helpers import (limpiar_consola, cabecera_menu, pedir_nombre, pedir_id, pedir_telefono,
                               definir_clave, definir_rol, hashear_clave, guion_titulo, guion_item, 
                               guion_sub_item, pausar_consola)


def pedir_dni():
    dni = input(f'|{" "*20}#-DNI: ')
    if dni == "":
        raise OperacionCancelada()
    elif not dni.isdigit():
        raise DatoNumericoObligatorio()
    elif len(dni) > 10:
        raise NumeroDemasiadoAlto()
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
            Gestion_Usuario().validar_dni(dni)    
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



def listar_usuarios(usuarios=None):
    if usuarios is None:
        usuarios = Gestion_Usuario().extraer_usuarios()

    if not usuarios:
        raise ArchivoVacio('No Se Encontraron Usuarios')
    for user in usuarios:
        print(user)


def listar_usuarios_activos():
    cabecera_menu()
    activos = Gestion_Usuario().extraer_activos()
    if activos:
        listar_usuarios(activos)


def listar_usuarios_suspendidos():
    cabecera_menu()
    suspendidos = Gestion_Usuario().extraer_suspendidos()
    if not suspendidos:
        raise ArchivoVacio('No Se Encontraron Usuarios')
    listar_usuarios(suspendidos)


def buscar_usuario(usuarios, id_usuario):
    for user in usuarios:
        if user.id_usuario == id_usuario:
            return user
    return None


def suspender_usuario():
    try:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('SUSPENCION DE USUARIOS')
        listar_usuarios()
        guion_item('Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))

        usuarios = Gestion_Usuario().extraer_usuarios()
        user = buscar_usuario(usuarios, id_buscar)
        if user is None or user.verificar_permisos():       # al administrador no se lo suspende
            raise IdNoEncontrado('No se encontro el usuario')

        limpiar_consola()
        cabecera_menu()
        print(user)
        guion_sub_item(" *Esta seguro que quiere suspender este Usuario?")
        guion_sub_item('  *Para confirmar, ingrese el DNI del usuario')
        if pedir_dni() != user.dni:
            raise OperacionCancelada()

        user.baja_usuario()
        Gestion_Usuario().escribir_usuarios(usuarios)
        pausar_consola("Se Suspendio el usuario exitosamente!")
    except TecStoreError as er:
        pausar_consola(er.mensaje)


def reactivar_usuario():
    try:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('REACTIVACION DE USUARIOS')
        listar_usuarios_suspendidos()
        guion_item('Ingrese el Id del Usuario')
        id_buscar = pedir_id(input('|##-· ID: '))

        usuarios = Gestion_Usuario().extraer_usuarios()
        user = buscar_usuario(usuarios, id_buscar)
        if user is None or user.validar_estado():           # solo se reactivan los suspendidos
            raise IdNoEncontrado('No se encontro el usuario')

        limpiar_consola()
        cabecera_menu()
        print(user)
        guion_sub_item(" *Esta seguro que quiere Reactivar este Usuario?")
        guion_sub_item(' *Para confirmar, ingrese el DNI del usuario')
        if pedir_dni() != user.dni:
            raise OperacionCancelada()

        user.reactivacion_usuario()
        Gestion_Usuario().escribir_usuarios(usuarios)
        pausar_consola("Se Reactivo el usuario exitosamente!")
    except TecStoreError as er:
        pausar_consola(er.mensaje)