from src.utils.Consola import menuPrincipal, Login, menu_registrar_usuario, Login

from src.utils import limpiar_consola

#   _________________
#|--| Menu de Inicio|-----------------------------------------------------

if __name__ == "__main__":

    #menu_registrar_usuario()


    logueo = Login()

    if logueo:
        menuPrincipal(logueo)
    