from datetime import datetime

class Venta:
    def __init__(self, id_venta, forma_pago, importe_total, fecha = None):
        self.id_venta = id_venta
        self.forma_pago = forma_pago
        self.importe_total = importe_total
        self.fecha = fecha if fecha is not None else datetime.now()
        


    def to_dict(self):
        diccionario = {
            "id_venta": self.id_venta,
            "forma_pago": self.forma_pago,
            "importe_total": self.importe_total,
            "fecha": str(self.fecha)
        }
        return diccionario


    def __str__(self):
        linea = f'o- VENTA NROº: {self.id_venta}'
        linea += f'\n - Fecha: {self.fecha.strftime("%d/%m/%Y %H:%M:%S")}'
        linea += f'\n - Total: ${self.importe_total:,}'
        linea += f'\n - Forma de pago: {self.forma_pago}'
        linea += '\n-········································'

        return linea

    def descuento_porcentaje(self, descuento):
       self.importe_total =self.importe_total - descuento

    def descuento_importe(self, descuento):
       self.importe_total = float(self.importe_total)-(float(self.importe_total)*(descuento/100))