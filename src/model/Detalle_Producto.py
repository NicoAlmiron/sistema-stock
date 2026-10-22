from src.utils.Helpers import dar_formato_nombre
from src.exceptions.excepciones import DatoInvalidoError


class Detalle_Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
        self.cantidad = cantidad

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor <= 0:
            raise DatoInvalidoError()
        self._cantidad = valor

    @property
    def subtotal(self):
        return self._precio * self._cantidad      

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "subtotal": self.subtotal          
        }

    def __str__(self):
        esp = 45 - (len(str(self.cantidad)) + len(str(self.subtotal)))
        return f'|     + {self.nombre.upper()}{dar_formato_nombre(self.nombre)} x {self.cantidad} - ${self.subtotal:,}{" " * esp}|'

    @classmethod
    def from_dict(cls, det_venta):
        return cls(
            id_producto=det_venta["id_producto"],
            nombre=det_venta["nombre"],
            precio=det_venta["precio"],
            cantidad=det_venta["cantidad"])