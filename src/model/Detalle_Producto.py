from .Producto import Producto
from src.utils.Helpers import dar_formato_nombre

class Detalle_Producto(Producto):
    def __init__(self, id_producto, nombre, precio, cantidad, subtotal):
        super().__init__(id_producto, nombre, precio, stock=None)
        self.cantidad = cantidad
        self.subtotal = subtotal
        

    def to_dict(self):
        diccionario = {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "subtotal": self.subtotal
        }
        return diccionario



    def __str__(self):
        esp = 45 - ( len(str(self.cantidad)) + len(str(self.subtotal)) )
        linea = f'|     + {self.nombre.upper()}{dar_formato_nombre(self.nombre)} x {self.cantidad} - ${self.subtotal:,}{" "* esp }|'
        return linea

    def to_str_carrito(self):
        print(f'||-{self.nombre} x {self.cantidad}|')

    @classmethod
    def from_dict(self, det_venta):
        detalle_venta = Detalle_Producto(  
            id_producto = det_venta["id_producto"], 
            nombre = det_venta["nombre"], 
            precio = det_venta["precio"], 
            cantidad = det_venta['cantidad'], 
            subtotal = det_venta['subtotal'])
        return detalle_venta

    