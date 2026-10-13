from src.classes import Venta, DetalleVenta
#from src.utils.Helpers import lista_Clases_a_diccionario
import json

ARCHIVO_VENTAS_JSON = "src/data/historial_ventas.json"


#|--------  ARCHIVO VENTA   --------|#
#   _____________________________
#|--| Extraer ventas del archivo|-----------------------------------------------------

def extraer_ventas():
    
    try:
        ventas_dicc = []
        
        with open(ARCHIVO_VENTAS_JSON, 'r', encoding='UTF-8') as arch_venta: 
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
                    det_vent_item["id_producto"], 
                    det_vent_item["nombre"], 
                    det_vent_item["precio"], 
                    det_vent_item["stock"], 
                    det_vent_item['cantidad'], 
                    det_vent_item['subtotal'])
                detalles_ventas.append(det_vent)

            venta = Venta(
                int(venta_item["id_venta"]), 
                venta_item["forma_pago"], 
                venta_item["importe_total"], 
                int(venta_item["id_vendedor"]), 
                venta_item["fecha"], 
                detalles_ventas)
                
            lista_ventas.append(venta)
        
    except FileNotFoundError:
        input("No se encontro el archivo")
        return []

    return lista_ventas



#   _____________________________
#|--| Guardar ventas del archivo|-----------------------------------------------------

def escribir_venta(ventas):

    lis_dic_venta = []

    for venta in ventas:
        lis_dic_venta.append(venta.to_dict())

    try:
        with open(ARCHIVO_VENTAS_JSON, 'w', encoding='UTF-8') as arch_venta: #, open(ARCHIVO_DETALLES_VENTAS_JSON, 'w', encoding='UTF-8') as arch_detalle_venta:
            json.dump(lis_dic_venta, arch_venta, indent=4)
            #arch_venta.write(ventas_json)
    except FileNotFoundError:
        print("Ocurrio un error al crear el archivo!")




