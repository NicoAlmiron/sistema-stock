from src.model.Detalle_Venta import Detalle_Venta
from src.model.Detalle_Producto import Detalle_Producto
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
                
                lista_ventas = []
                for venta_item in ventas_dicc:
                    detalles_ventas = []
                    for det_vent_item in venta_item["detalle_venta"]:
                        #det_vent = None
                        det_prod = Detalle_Producto(None,None,None,None,None).from_dict(det_vent_item)
                        detalles_ventas.append(det_prod)
                    det_venta = Detalle_Venta(None,None,None,None,None,None).from_dict(venta_item, detalles_ventas)   
                    lista_ventas.append(det_venta)

            return lista_ventas
        except FileNotFoundError:
            return []
        except Exception:
            return []



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
        except Exception:
            return False
            


    def definir_id(self):
        ventas = self.extraer_ventas()
        if not ventas:
            return 1
        return max(v.id_venta for v in ventas) + 1




