from src.classes.Sesion import Sesion
from src.persistensia.Actividad_JSON import extraer_historial_actividad, escribir_historial_actividad
from datetime import datetime

def definir_id():
    hist_actv =  extraer_historial_actividad()

    if not hist_actv:
        return 1
    
    return max(h.id_sesion for h in hist_actv) + 1


def crear_sesion(user):
    id_sesion = definir_id()
    sesion_activa = Sesion(user.id_usuario, user.nombre, user.dni, user.telefono, user.rol, id_sesion)
    return sesion_activa

def cerrar_sesion(sesion):
    sesion.prods_vendidos = 10 #cant_prod_vend(sesion)
    sesion.monto_bruto = 345000 #mon_tot_vend(sesion)
    sesion.fin_actividad = datetime.now()
    escribir_historial_actividad(sesion)

    