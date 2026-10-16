from datetime import datetime

class Venta:
    def __init__(self, id_venta, forma_pago, importe_total, id_vendedor, vendedor_nombre, detalle_venta, cliente = None, fecha = None):
        self.id_venta = id_venta
        self.forma_pago = forma_pago
        self.importe_total = importe_total
        self.id_vendedor = id_vendedor
        self.fecha = fecha if fecha is not None else datetime.now()
        self.vendedor_nombre = vendedor_nombre
        self.cliente = cliente if cliente is not None else ""
        self.detalle_venta = detalle_venta


    def to_dict(self):
        diccionario = {
            "id_venta": self.id_venta,
            "forma_pago": self.forma_pago,
            "importe_total": self.importe_total,
            "id_vendedor": self.id_vendedor,
            "vendedor_nombre": self.vendedor_nombre,
            "cliente": self.cliente,
            "fecha": str(self.fecha),
            "detalle_venta": [d.to_dict() for d in self.detalle_venta]
        }
        return diccionario


    def __str__(self):
        linea = f'o- VENTA NROº: {self.id_venta}'
        linea += f'\n - Cajero: {self.vendedor_nombre}'
        linea += f'\n - Fecha: {self.fecha.strftime("%d/%m/%Y %H:%M:%S")}'
        linea += F'\n - Cliente: {self.cliente}'
        linea += '\n - Productos:'
        for prod_vent in self.detalle_venta:
            precio_prod = f'{prod_vent.precio:,}'
            linea += f'\n     ·{prod_vent.nombre}{(" " * ( 30 - len(prod_vent.nombre) ) )}- ${precio_prod}{(" " * ( 11 - len(precio_prod) ) )} - x {prod_vent.cantidad} - SubTotal ${prod_vent.subtotal:,} '
        linea += f'\n - Total: ${self.importe_total:,}'
        linea += f'\n - Forma de pago: {self.forma_pago}'
        linea += '\n-········································'

        return linea

    def descuento_porcentaje(self, descuento):
       self.importe_total =self.importe_total - descuento

    def descuento_importe(self, descuento):
       self.importe_total = float(self.importe_total)-(float(self.importe_total)*(descuento/100))