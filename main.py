from src.utils.Consola import menuPrincipal
from src.services.Actividad_services import Login
from src.persistensia.Gestion_Sesion import Gestion_Sesion

if __name__ == "__main__":

    sesion = Login()

    try:
        menuPrincipal(sesion)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido...")
    #finally:
        # Pase lo que pase (salida normal, Ctrl+C o un error), la sesion queda guardada
        #Gestion_Sesion().guardar_sesion(sesion)