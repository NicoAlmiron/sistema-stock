from src.model.Venta import Venta
from src.model.Detalle_Venta import DetalleVenta
import json


class Gestion_Venta():
    def __init__(self, venta=None, productos=None):
        self.venta = venta
        self.productos = productos
        self.arch_json = "src/data/historial_ventas.json"

    #|--------  ARCHIVO VENTA   --------|#
#   _____________________________
#|--| Extraer ventas del archivo|-----------------------------------------------------

    def extraer_ventas(self):
        
        try:
            ventas_dicc = []
            
            with open(self.arch_json, 'r', encoding='UTF-8') as arch_venta: 
                ventas_dicc = json.load(arch_venta)
                #detalles_ventas = json.load(arch_detalle_venta)

                if len(ventas_dicc) <= 0:
                    return []
                
            lista_ventas = []
            for venta_item in ventas_dicc:
                detalles_ventas = []
                for det_vent_item in venta_item["detalle_venta"]:
                    det_vent = None
                    det_vent = DetalleVenta( 
                        id_venta = det_vent_item["id_venta"], 
                        id_producto = det_vent_item["id_producto"], 
                        nombre = det_vent_item["nombre"], 
                        precio = det_vent_item["precio"], 
                        cantidad = det_vent_item['cantidad'], 
                        subtotal = det_vent_item['subtotal'])
                    detalles_ventas.append(det_vent)

                venta = Venta(
                    id_venta =int(venta_item["id_venta"]), 
                    forma_pago = venta_item["forma_pago"], 
                    importe_total = venta_item["importe_total"], 
                    id_vendedor = int(venta_item["id_vendedor"]), 
                    vendedor_nombre = int(venta_item["vendedor_nombre"]), 
                    cliente = int(venta_item["cliente"]), 
                    fecha = venta_item["fecha"], 
                    detalle_venta = detalles_ventas)
                    
                lista_ventas.append(venta)
            
        except FileNotFoundError:
            return []

        return lista_ventas



#   _____________________________
#|--| Guardar ventas del archivo|-----------------------------------------------------

    def procesar_venta(self):

        ventas = self.extraer_ventas()
        lis_dic_venta = []

        for venta in ventas:
            lis_dic_venta.append(venta.to_dict())

        try:
            with open(self.arch_json, 'w', encoding='UTF-8') as arch_venta: #, open(ARCHIVO_DETALLES_VENTAS_JSON, 'w', encoding='UTF-8') as arch_detalle_venta:
                json.dump(lis_dic_venta, arch_venta, indent=4)
                #arch_venta.write(ventas_json)
        except FileNotFoundError:
            print("Ocurrio un error al crear el archivo!")


    def definir_id(self):
        ventas = self.extraer_ventas()
        if not ventas:
            return 1
        return max(v.id_venta for v in ventas) + 1



