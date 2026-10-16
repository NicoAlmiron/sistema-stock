from .Producto import Producto
from .Venta import Venta
from src.utils.Helpers import dar_formato_nombre

class DetalleVenta(Producto, Venta):
    def __init__(self, id_producto, nombre, precio, cantidad, subtotal, id_venta, stock = None, importe_total = None, forma_pago = None, id_vendedor = None, vendedor_nombre = None, detalle_Venta = None):
        super().__init__(id_producto, nombre, precio, stock)
        super().__init__( id_venta, forma_pago, importe_total, id_vendedor, vendedor_nombre, detalle_Venta)
        self.cantidad = cantidad
        self.subtotal = subtotal
        

    def to_dict(self):
        diccionario = {
            "id_venta": self.id_venta,
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "subtotal": self.subtotal
        }
        return diccionario



    def to_str(self):
        linea = f'|-{self.nombre}{dar_formato_nombre(self.nombre)} x {self.cantidad} - ${self.subtotal:,}'
        return linea

    def to_str_carrito(self):
        print(f'||-{self.nombre} x {self.cantidad}')


    def from_dict(self, det_venta):
        detalle_venta = DetalleVenta( 
            id_venta = det_venta["id_venta"], 
            id_producto = det_venta["id_producto"], 
            nombre = det_venta["nombre"], 
            precio = det_venta["precio"], 
            cantidad = det_venta['cantidad'], 
            subtotal = det_venta['subtotal'])
        return detalle_venta

    