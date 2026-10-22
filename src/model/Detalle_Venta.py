from datetime import datetime
from .Venta import Venta
from src.utils.Helpers import guion_item, dar_formato_nombre, dar_formato_precio, pausar_consola

class Detalle_Venta(Venta):
    def __init__(self, id_venta, forma_pago, importe_total, id_vendedor, vendedor_nombre, detalle_venta, cliente=None, fecha=None, importe_sin_desc=None, descuento_tipo=None, desc_monto=None, desc_tipo_importe=None, desc_tipo_porcentual=None):
        super().__init__(id_venta, forma_pago, importe_total, fecha, importe_sin_desc, descuento_tipo, desc_monto, desc_tipo_importe, desc_tipo_porcentual)
        self.id_vendedor = id_vendedor
        self.vendedor_nombre = vendedor_nombre
        self.cliente = cliente if cliente is not None else ""
        self.detalle_venta = detalle_venta


    def to_dict(self):
            diccionario = {
                "id_venta": self.id_venta,
                "id_vendedor": self.id_vendedor,
                "vendedor_nombre": self.vendedor_nombre,
                "cliente": self.cliente,
                "forma_pago": self.forma_pago,
                "importe_sin_desc": self.importe_sin_desc,
                "descuento_tipo": self.descuento_tipo,
                "desc_monto": self.desc_monto,
                "desc_tipo_importe": self.desc_tipo_importe,            
                "desc_tipo_porcentual": self.desc_tipo_porcentual, 
                "importe_total": self.importe_total,
                "fecha": str(self.fecha),
                "detalle_venta": [d.to_dict() for d in self.detalle_venta]
            }
            return diccionario

    def __str__(self):
            linea = f'|{"-"*17}> VENTA NRO: {self.id_venta}{" "* (60-len(str(self.id_venta)))}|'
            linea += f'\n|{" "*15} ·> Cajero: {self.vendedor_nombre}{" "* (63-len(self.vendedor_nombre))}|'
            linea += f'\n|{" "*15} ·> Fecha: {self.fecha.strftime("%d/%m/%Y %H:%M:%S")}{" "* (64-len(self.fecha.strftime("%d/%m/%Y %H:%M:%S")))}|'
            linea += f'\n|{" "*15} ·> Cliente: {self.cliente}{" "* (62-len(self.cliente))}|'
            linea += f'\n|{" "*15} ·>Forma de Pago: {self.forma_pago}{" "*(57-len(self.forma_pago))}|'
            linea += f'\n|{" "*15} ·>Total Bruto: ${self.importe_sin_desc:,}{" "*(57-len(str(self.importe_sin_desc)))}|'
            if self.descuento_tipo:
                if self.descuento_tipo == "PORCENTUAL": 
                    linea += f'\n|{" "*15} ·> Descuento: %{self.desc_tipo_porcentual}{" "*(59-(len(str(self.desc_tipo_porcentual))))}|'
                elif self.descuento_tipo == "IMPORTE": 
                    linea += f'\n|{" "*15} ·> Importe de Descuento{" "* 51}|'
                linea += f'\n|{" "*15} ·> descontado: -${self.desc_monto:,}{" "* (56-len(str(self.desc_monto)))}|'
                linea += f'\n|{" "*15} ·> Total Neto: ${self.importe_total:,}{" "* (57-len(str(self.importe_total)))}|'
            linea += f'\n|{" "*10}·> PRODUCTOS{" " * 68}|'
            for prod_vent in self.detalle_venta:
                            precio_prod = f'{prod_vent.precio:,}'
                            linea += f'\n|{" "*10}·{prod_vent.nombre}{(" " * ( 30 - len(prod_vent.nombre) ) )}'
                            linea += f' - ${precio_prod}{(" " * ( 11 - len(precio_prod) ) )}'
                            linea += f'- x {prod_vent.cantidad} - SubTotal ${prod_vent.subtotal:,}'
                            linea += f'{" " * (16 - (len(str(prod_vent.cantidad)) + len(str(prod_vent.subtotal)))) }|'
            linea += f'\n|##{"·"*20}{" "*46}{"·"*20}##|'
            
            return linea

    @classmethod
    def from_dict(cls, venta_item, detalles_ventas):
        return cls(
            id_venta =int(venta_item["id_venta"]), 
            id_vendedor = int(venta_item["id_vendedor"]), 
            vendedor_nombre = venta_item["vendedor_nombre"], 
            cliente = venta_item["cliente"], 
            forma_pago = venta_item["forma_pago"], 
            importe_sin_desc = float(venta_item["importe_sin_desc"]) if venta_item["importe_sin_desc"] is not None else "" , 
            descuento_tipo = venta_item["descuento_tipo"], 
            desc_monto = float(venta_item["desc_monto"]) if venta_item["desc_monto"] is not None else None, 
            desc_tipo_importe = float(venta_item["desc_tipo_importe"]) if venta_item["desc_tipo_importe"] is not None else None,
            desc_tipo_porcentual = int(venta_item["desc_tipo_porcentual"]) if venta_item["desc_tipo_porcentual"] is not None else None, 
            importe_total = float(venta_item["importe_total"]) if venta_item["importe_total"] is not None else None,
            fecha = datetime.fromisoformat(venta_item["fecha"]),
            detalle_venta = detalles_ventas)
        

    def resumen_venta(self, desc):
        guion_item("RESUMEN DE LA VENTA")
        print('|-- Productos')
            
        for prod in self.detalle_venta:
            #prod_dicc = lista_prods[i]
            prcio_prod = f'{prod.precio:,}'
            linea = f"|    + {prod.nombre.upper()}{dar_formato_nombre(prod.nombre)}"
            linea += f'${prcio_prod}{dar_formato_precio(prcio_prod)} C/U'
            linea += f' x {prod.cantidad} - ${prod.subtotal:,}{" " * (28 - (len(str(prod.cantidad))+len(str(prod.subtotal))) )}|'
            print(linea)
                                    
        print(f'|-- Total: ${self.importe_sin_desc:,}{" "*(79-(len(str(self.importe_sin_desc))))}|')
        if desc: 
            print(f'|-- Descuento: -${self.desc_monto:,}{" "*(73-(len(str(self.desc_monto))))}|')
            print(f'|-- Total Neto(Descuento): ${self.importe_total:,}{" "*(62-(len(str(self.importe_total))))}|')
        print(f'|-- Forma de pago: {self.forma_pago}{" "*(71-(len(str(self.forma_pago))))}|')
        pausar_consola()