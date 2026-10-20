from src.utils.Helpers import limpiar_consola, cabecera_menu, guion_titulo, guion_base, pausar_consola
from src.persistensia.Gestion_Usuario import Gestion_Usuario
from src.persistensia.Gestion_Sesion import Gestion_Sesion
from src.exceptions.excepciones import AuthenticationError


def Login():
    while True:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('INICIO DE SESION')
        guion_base()
        dni =   input('|\t\t\t\t#-DNI:         ')
        clave = input('|\t\t\t\t#-CONTRASEÑA:  ')
        limpiar_consola()
        cabecera_menu()
        try:
            user = Gestion_Usuario().autenticar_usuario(dni, clave)
            guion_titulo(f'BIENVENIDO {user.nombre}')
            pausar_consola()
            sesion_activa = Gestion_Sesion().crear_sesion(user)
            return sesion_activa
        except AuthenticationError as e:
            guion_base()
            guion_titulo(e.mensaje_default)
            guion_base()
            pausar_consola()
