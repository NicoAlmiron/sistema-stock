from src.utils.Helpers import limpiar_consola, cabecera_menu
from src.persistensia.Gestion_Usuario import Gestion_Usuario
from src.persistensia.Gestion_Sesion import Gestion_Sesion
from src.persistensia.Gestion_Venta import Gestion_Venta
from src.exceptions.excepciones import AuthenticationError


def Login():
    while True:
        limpiar_consola()
        cabecera_menu()
        print('|##···INICIO DE SESION···##|')
        dni = input('|#-DNI: ')
        clave = input('|#-CONTRASEÑA: ')
        limpiar_consola()
        cabecera_menu()
        try:
            user = Gestion_Usuario().autenticar_usuario(dni, clave)
            print(f'|# BIENVENIDO {user.nombre}')
            input( '|##······················##|')
            sesion_activa = Gestion_Sesion().crear_sesion(user)
            return sesion_activa
        except AuthenticationError as e:
            print(e)
            input( '|##······················##|')
