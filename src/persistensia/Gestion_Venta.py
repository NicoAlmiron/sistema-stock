from src.model.Venta import Venta
from datetime import datetime
from src.exceptions.excepciones import ErrorPersistencia
import json

class Gestion_Venta():
    def __init__(self, venta=None):
        self.venta = venta
        self.arch_json = "src/data/historial_ventas.json"

    #|--------  ARCHIVO VENTA   --------|#
#   _____________________________
#|--| Extraer ventas del archivo|-----------------------------------------------------
    def extraer_ventas(self):
        
        try:
            ventas_dicc = []
            with open(self.arch_json, 'r', encoding='UTF-8') as arch_venta: 
                ventas_dicc = json.load(arch_venta)
                if not ventas_dicc:
                    return []
                
                lista_ventas = [Venta.from_dict(item) for item in ventas_dicc]

            return lista_ventas
        except FileNotFoundError:
            return []
        except:
            raise ErrorPersistencia()



#   _____________________________
#|--| Guardar ventas del archivo|-----------------------------------------------------
    def procesar_venta(self, venta_nueva):

        ventas = self.extraer_ventas()
        lis_dic_venta = []

        for venta in ventas:
            lis_dic_venta.append(venta.to_dict())

        lis_dic_venta.append(venta_nueva.to_dict())

        try:
            with open(self.arch_json, 'w', encoding='UTF-8') as arch_venta: 
                ventas_json = json.dumps(lis_dic_venta, indent=4)
                arch_venta.write(ventas_json)
                return True
        except FileNotFoundError:
            with open(self.arch_json, 'w', encoding='UTF-8') as arch_venta: 
                ventas_json = json.dumps(lis_dic_venta, indent=4)
                arch_venta.write(ventas_json)
                return True
        except:
            raise ErrorPersistencia()
            


    def definir_id(self):
        ventas = self.extraer_ventas()
        if not ventas:
            return 1
        return max(v.id_venta for v in ventas) + 1


    def extraer_ventas_en_rango(self, desde, hasta=None, id_vendedor=None):
        hasta = hasta if hasta is not None else datetime.now() # si no trae el "hasta" pone el momento actual

        return [
            v for v in self.extraer_ventas()    
            
            if desde <= v.fecha <= hasta 
            and (id_vendedor is None or v.id_vendedor == id_vendedor) 
        ]    



