from src.model.Sesion import Sesion
from .Gestion_Venta import Gestion_Venta
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
                    
                for user_sesion in lista_actv:
                    sesion = Sesion(None, None, None, None, None, None).from_dict(user_sesion)
                    historial_actividad.append(sesion)

            return historial_actividad
        except FileNotFoundError:
            input("Archivo Json no encontrado!")
            return []
        #except Exception as er:
            #input(er)


    def escribir_historial_actividad(self, sesion):
        lista_dicc = []
        historial_actividad = self.extraer_historial_actividad()

        for actv in historial_actividad:
            lista_dicc.append(actv.to_dict())
        lista_dicc.append(sesion.to_dict())


        try:
            with open(self.arch_json , 'w', encoding='UTF-8') as actividad_json:
                arch_json = json.dumps(
                    lista_dicc,
                    indent=4)
                actividad_json.write(arch_json)
            return True
        except FileNotFoundError:
            with open(self.arch_json , 'w', encoding='UTF-8') as actividad_json:
                arch_json = json.dumps(
                    lista_dicc,
                    indent=4)
                actividad_json.write(arch_json)
            return True
        except Exception as er:
            input("A sucedido un error inesperado!")
            #return False
        
    def definir_id(self):
        hist_actv =  self.extraer_historial_actividad()

        if not hist_actv:
            return 1
        
        return max(h.id_sesion for h in hist_actv) + 1

    def crear_sesion(self, user):
        id_sesion = self.definir_id()
        sesion_activa = Sesion(id_usuario=user.id_usuario, nombre=user.nombre, dni=user.dni, telefono=user.telefono, rol=user.rol, id_sesion=id_sesion)
        return sesion_activa

    def guardar_sesion(self, sesion):
        ventas = Gestion_Venta().extraer_ventas_en_rango(desde=sesion.inicio_actividad,id_vendedor=sesion.id_usuario) #cant_prod_vend(sesion)
        sesion.prods_vendidos = sum(dv.cantidad for v in ventas for dv in v.detalle_venta)
        sesion.monto_bruto = sum(dv.subtotal for v in ventas for dv in v.detalle_venta)
        sesion.monto_neto = sum(v.importe_total for v in ventas)
        sesion.fin_actividad = datetime.now()
        self.escribir_historial_actividad(sesion)