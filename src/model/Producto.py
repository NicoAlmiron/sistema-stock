from src.utils.Helpers import dar_formato_id, dar_formato_precio, dar_formato_nombre, pedir_nombre, pedir_precio, pedir_stock
from src.exceptions.excepciones import StockInsuficiente, OperacionCancelada
from src.exceptions.excepciones import (StockInsuficiente, NombreInvalido, PrecioNegativoError,
                                        PrecioDemaciadoAlto, NumeroNegativoError, NumeroDemasiadoAlto)

class Producto:
    NOMBRE_MAX = 30
    PRECIO_MAX = 99_999_999_999
    STOCK_MAX = 9_999

    def __init__(self, id_producto, nombre, precio, stock, cant_vendidos=None, discontinuado=False):
        self._id_producto = id_producto
        self.nombre = nombre          # pasa por el setter, que valida
        self.precio = precio
        self.stock = stock
        self.discontinuado = discontinuado
        self.cant_vendidos = cant_vendidos if cant_vendidos is not None else 0

    @property
    def id_producto(self):
        return self._id_producto      # solo lectura

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        valor = str(valor).strip()
        if not valor or len(valor) > self.NOMBRE_MAX:
            raise NombreInvalido()
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise PrecioNegativoError()
        if valor > self.PRECIO_MAX:
            raise PrecioDemaciadoAlto()
        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise NumeroNegativoError()
        if valor > self.STOCK_MAX:
            raise NumeroDemasiadoAlto()
        self._stock = valor
        
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

    @classmethod
    def from_dict(cls, prod):
        return cls(
                        id_producto = int(prod["id_producto"]),
                        nombre = prod["nombre"],
                        precio = float(prod["precio"]),
                        cant_vendidos =int(prod["cant_vendidos"]),
                        discontinuado = bool(prod["discontinuado"]),
                        stock = int(prod["stock"]) 
                    )

    def verificar_stock(self, cant_compra):
        if self.stock and self.stock >= cant_compra:
            return True
        else:
            raise StockInsuficiente()

    def descontar_stock(self, cantidad):
        if cantidad > self.stock:
            raise StockInsuficiente()
        self.stock -= cantidad
        self.cant_vendidos += cantidad

    def discontinuar_producto(self):
        if not self.discontinuado:
            self.discontinuado = True

    def reactivar_producto(self):
        if self.discontinuado:
            self.discontinuado = False

    