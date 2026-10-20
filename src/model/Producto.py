from src.utils.Helpers import dar_formato_id, dar_formato_precio, dar_formato_nombre, pedir_nombre, pedir_precio, pedir_stock
from src.exceptions.excepciones import StockInsuficiente, OperacionCancelada

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
        renglon = f'| -> ID: {self.id_producto}{dar_formato_id(self.id_producto)}'
        renglon += f'| {self.nombre}{dar_formato_nombre(self.nombre)}'
        renglon += f'| ${precio_prod}{dar_formato_precio(precio_prod)}'
        #renglon += f'| VENDIDOS: {self.cant_vendidos}{dar_formato_id(self.cant_vendidos)}'

        if self.discontinuado:
            renglon += '| PRODUCTO DISCONTINUADO'
        elif int(self.stock) < 4 and int(self.stock) > 0:
            renglon += f'| STOCK: {self.stock} STOCK BAJO{" "*(8- len(str(self.stock)))}|'
        elif int(self.stock) == 0:
            renglon += f'| STOCK: {self.stock} *SIN STOCK*{" "*(7- len(str(self.stock)))}|'
        else :
            renglon += f'| STOCK: {self.stock}{" "*(19- len(str(self.stock)))}|'
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

    def verificar_stock(self, cant_compra):
        if self.stock and self.stock >= cant_compra:
            return True
        else:
            raise StockInsuficiente()

    def desc_stock(self, cantidad):
        self.stock = self.stock - cantidad

    def modificar_producto(self):
        print(f'|##-· Producto ID: {self.id_producto}')
        try:
            print(f"|-Nobre anterior *{self.nombre}*")
            self.nombre = pedir_nombre(input('|-Nobre del articulo: '))
        except OperacionCancelada:
            pass
        try:    
            print(f"|-Precio anterior $*{self.precio:,}*".replace(",","."))
            self.precio = pedir_precio(input('|-Precio: $'))
        except OperacionCancelada:
            pass

    def modificar_stock(self):
        print(f'|##-· Producto ID: {self.id_producto}')
        try:
            print(f"| {self.nombre}*")
            print(f"| -Stock actual *{self.stock}*")
            self.stock = pedir_stock(input('|-Nuevo Stock: '))
        except OperacionCancelada:
            pass


    def discontinuar_producto(self):
        if not self.discontinuado:
            self.discontinuado = True
        else:
            raise OperacionCancelada("|· Producto ya discontinuado")

    def reactivar_producto(self):
        if self.discontinuado:
            self.discontinuado = False
        else:
            raise OperacionCancelada("|· Producto Activo")

    