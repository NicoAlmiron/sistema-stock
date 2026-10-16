from src.model.Sesion import Sesion
import json
from datetime import datetime


class Gestion_Sesion():
    def __init__(self):
        self.arch_json = "src/data/historial_actividad.json"

    def extraer_historial_actividad(self):
        try:
            historial_actividad = [] 

            with open(self.arch_json , 'r', encoding='UTF-8') as actividad_json:
                lista_actv = json.load(actividad_json)

                if len(lista_actv) == 0:
                    return []
                    
                for user in lista_actv:
        
                    sesion = Sesion().to_dict(user)
        
                    historial_actividad.append(sesion)
            return historial_actividad
        except FileNotFoundError:
            input("Archivo Json no encontrado!")
            return []
        except:
            return []


    def escribir_historial_actividad(self, sesion):
        lista_dicc = []
        historial_actividad = self.extraer_historial_actividad()
        historial_actividad.append(sesion)
        for actv in historial_actividad:
            lista_dicc.append(actv.to_dict())


        try:
            with open(self.arch_json , 'w', encoding='UTF-8') as actividad_json:
                arch_json = json.dumps(
                    lista_dicc,
                    indent=4)
                actividad_json.write(arch_json)
            #return True
        except FileNotFoundError:
            with open(self.arch_json , 'w', encoding='UTF-8') as actividad_json:
                arch_json = json.dumps(
                    lista_dicc,
                    indent=4)
                actividad_json.write(arch_json)
            #return True
        except:
            input("A sucedido un error inesperado!")
            #return False
        
    def definir_id(self):
        hist_actv =  self.extraer_historial_actividad()

        if not hist_actv:
            return 1
        
        return max(h.id_sesion for h in hist_actv) + 1

    def crear_sesion(self, user):
        id_sesion = self.definir_id()
        sesion_activa = Sesion(user.id_usuario, user.nombre, user.dni, user.telefono, user.rol, id_sesion=id_sesion)
        return sesion_activa

    def guardar_sesion(self, sesion):
        sesion.prods_vendidos = 10 #cant_prod_vend(sesion)
        sesion.monto_bruto = 345000 #mon_tot_vend(sesion)
        sesion.fin_actividad = datetime.now()
        self.escribir_historial_actividad(sesion)