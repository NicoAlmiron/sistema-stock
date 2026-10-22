from src.utils.Consola import menuPrincipal
from src.services.Actividad_services import Login

if __name__ == "__main__":

    logueo = Login()

    if logueo:
        menuPrincipal(logueo)
    