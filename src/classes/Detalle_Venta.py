from .Producto import Producto

class DetalleVenta(Producto):
    def __init__(self, id_producto, nombre, precio, stock, cantidad, subtotal):
        super().__init__(id_producto, nombre, precio, stock)
        self.cantidad = cantidad
        self.subtotal = subtotal

    def to_dict(self):
        diccionario = {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "cantidad": self.cantidad,
            "subtotal": self.subtotal
        }
        return diccionario
        

