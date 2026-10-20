from datetime import datetime

class Venta:
    def __init__(self, id_venta, forma_pago, importe_total, fecha = None, importe_sin_desc = None, descuento_tipo = None, desc_monto = None, desc_tipo_importe = None, desc_tipo_porcentual=None):
        self.id_venta = id_venta
        self.forma_pago = forma_pago
        self.importe_total = importe_total
        self.importe_sin_desc = importe_sin_desc
        self.descuento_tipo = descuento_tipo
        self.desc_monto = desc_monto
        self.desc_tipo_importe = desc_tipo_importe
        self.desc_tipo_porcentual = desc_tipo_porcentual
        self.fecha = fecha if fecha is not None else datetime.now()
        


    def to_dict(self):
        diccionario = {
            "id_venta": self.id_venta,
            "forma_pago": self.forma_pago,
            "importe_total": self.importe_total,
            "importe_sin_desc": self.importe_sin_desc,
            "descuento_tipo": self.descuento_tipo,
            "desc_monto": self.desc_monto,
            "desc_tipo_importe": self.desc_tipo_importe,            
            "desc_tipo_porcentual": self.desc_tipo_porcentual,            
            "fecha": str(self.fecha)
        }
        return diccionario


    def __str__(self):
        linea = f'o- VENTA NROº: {self.id_venta}'
        linea += f'\n - Forma de pago: {self.forma_pago}'
        linea += f'\n - Total: ${self.importe_sin_desc:,}'
        if self.descuento_tipo:
            if self.descuento_tipo == "PORCENTUAL": linea += f'\n - Descuento: %{self.desc_tipo_porcentual}'
            if self.descuento_tipo == "IMPORTE": linea += f'\n - Descuento: ${self.desc_tipo_importe:,}'
            linea += f'\n - descontado: -${self.desc_monto:,}'
            linea += f'\n - Total Final: ${self.importe_total:,}'
        linea += f'\n - Fecha: {self.fecha.strftime("%d/%m/%Y %H:%M:%S")}'
        linea += '\n-········································'

        return linea

    def descuento_importe(self, descuento):
       self.descuento_tipo = "IMPORTE"
       self.desc_tipo_importe = descuento
       self.desc_monto = descuento
       self.importe_total = self.importe_sin_desc - descuento

    def descuento_porcentaje(self, descuento):
       self.descuento_tipo = "PORCENTUAL"
       self.desc_tipo_porcentual = descuento
       self.desc_monto = float(self.importe_sin_desc)*(descuento/100)
       self.importe_total = float(self.importe_sin_desc) - (float(self.importe_sin_desc)*(descuento/100))