from datetime import datetime

class Venta:
    def __init__(self, id_venta, forma_pago, importe_total, detalle_venta, id_vendedor, fecha = None):
        self.id_venta = id_venta
        self.forma_pago = forma_pago
        self.importe_total = importe_total
        self.detalle_venta = detalle_venta
        self.id_vendedor = id_vendedor
        self.fecha = fecha if fecha is not None else datetime.now()

    def to_dict(self):
        diccionario = {
            "id_venta": self.id_venta,
            "forma_pago": self.forma_pago,
            "importe_total": self.importe_total,
            "id_vendedor": self.id_vendedor,
            "fecha": str(self.fecha),
            "detalle_venta": [d.to_dict() for d in self.detalle_venta]
        }
        return diccionario

    def __str__(self):
        linea = f'o- Venta Nroº: {self.id_venta}'
        linea += '\n - Productos:'
        for prod_vent in self.detalle_venta:
            precio_prod = f'{prod_vent.precio:,}'
            linea += f'\n     ·{prod_vent.nombre}{(" " * ( 30 - len(prod_vent.nombre) ) )}- ${precio_prod}{(" " * ( 11 - len(precio_prod) ) )} - x {prod_vent.cantidad} - SubTotal ${prod_vent.subtotal:,} '
        linea += f'\n - Total: ${self.importe_total:,}'
        linea += f'\n - Forma de pago: {self.forma_pago}'
        linea += '\n-········································'

        return linea

        