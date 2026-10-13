from src.classes.Sesion import Sesion
import json
from datetime import datetime

ARCHIVO_ACTIVIDAD_JSON = "src/data/historial_actividad.json"


def extraer_historial_actividad():
    try:
        historial_actividad = [] 

        with open(ARCHIVO_ACTIVIDAD_JSON , 'r', encoding='UTF-8') as actividad_json:
            lista_actv = json.load(actividad_json)

            if len(lista_actv) == 0:
                return []
                
            for user in lista_actv:
    
                sesion = Sesion(
                    id_sesion=int(user["id_sesion"]),
                    id_usuario=int(user["id_usuario"]),
                    nombre=user["nombre"],
                    dni=user["dni"],
                    telefono=user["telefono"],
                    rol=user["rol"],
                    inicio_activididad=datetime.fromisoformat(user["inicio_activididad"]),
                    prods_vendidos=int(user["prods_vendidos"]),
                    monto_bruto=float(user["monto_bruto"]),
                    fin_actividad=datetime.fromisoformat(user["fin_actividad"])
                )
    
                historial_actividad.append(sesion)
        return historial_actividad
    except FileNotFoundError:
        input("Archivo Json no encontrado!")
        return []
    except:
        return []


def escribir_historial_actividad(sesion):
    lista_dicc = []
    historial_actividad = extraer_historial_actividad()
    historial_actividad.append(sesion)
    for actv in historial_actividad:
        lista_dicc.append(actv.to_dict())


    try:
        with open(ARCHIVO_ACTIVIDAD_JSON , 'w', encoding='UTF-8') as actividad_json:
            arch_json = json.dumps(
                lista_dicc,
                indent=4)
            actividad_json.write(arch_json)
        #return True
    except FileNotFoundError:
        with open(ARCHIVO_ACTIVIDAD_JSON , 'w', encoding='UTF-8') as actividad_json:
            arch_json = json.dumps(
                lista_dicc,
                indent=4)
            actividad_json.write(arch_json)
        #return True
    except:
        input("A sucedido un error inesperado!")
        #return False
    