from src.utils.Consola import menuPrincipal
from src.services.Actividad_services import Login

from src.utils import limpiar_consola

#   _________________
#|--| Menu de Inicio|-----------------------------------------------------

if __name__ == "__main__":

    #menu_registrar_usuario()


    logueo = Login()

    if logueo:
        menuPrincipal(logueo)
    