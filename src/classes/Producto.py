class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        
    def __str__(self):
        precio_prod = f'{self.precio:,}'
        renglon = f'|ID: {self.id_producto}{(" " * ( 6 - len(str(self.id_producto)) ) )}'
        renglon += f'| {self.nombre}{(" " * ( 30 - len(self.nombre) ) )}'
        renglon += f'| ${self.precio:,}{(" " * ( 13 - len(precio_prod)))}'
        renglon += f'| STOCK: {self.stock}'
        if int(self.stock) < 4 and int(self.stock) > 0:
            renglon += ' (STOCK BAJO)'
        elif int(self.stock) == 0:
            renglon += ' (SIN STOCK!!*!*!*!)'
        return renglon

    def to_dict(self):
            diccionario = {
                "id_producto": self.id_producto,
                "nombre": self.nombre,
                "precio": self.precio,
                "stock": self.stock
            }
            return diccionario