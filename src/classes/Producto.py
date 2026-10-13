from src.utils.Helpers import dar_formato_id, dar_formato_precio, dar_formato_nombre

class Producto:
    def __init__(self, id_producto, nombre, precio, stock, cant_vendidos = None, discontinuado = False):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.discontinuado = discontinuado
        self.cant_vendidos = cant_vendidos if cant_vendidos is not None else 0

        
    def __str__(self):
        precio_prod = f'{self.precio:,}'
        renglon = f'|ID: {self.id_producto}{dar_formato_id(self.id_producto)}'
        renglon += f'| {self.nombre}{dar_formato_nombre(self.nombre)}'
        renglon += f'| ${self.precio:,}{dar_formato_precio(precio_prod)}'
        renglon += f'| VENDIDOS: {self.cant_vendidos}{dar_formato_id(self.cant_vendidos)}'

        if self.discontinuado:
            renglon += '| PRODUCTO DISCONTINUADO'
        elif int(self.stock) < 4 and int(self.stock) > 0:
            renglon += f'| STOCK: {self.stock} (STOCK BAJO)'
        elif int(self.stock) == 0:
            renglon += f'| STOCK: {self.stock} (SIN STOCK!!*!*!*!)'
        else :
            renglon += f'| STOCK: {self.stock}'

        return renglon

    def to_dict(self):
            diccionario = {
                "id_producto": self.id_producto,
                "nombre": self.nombre,
                "precio": self.precio,
                "cant_vendidos": self.cant_vendidos,
                "discontinuado": self.discontinuado,
                "stock": self.stock
            }
            return diccionario