from src.model import Producto
from src.exceptions.excepciones import ArchivoVacio
from .Gestor_JSON import GestorJSON

class Gestion_Producto(GestorJSON):
    def __init__(self):
        super().__init__("src/data/productos.json")

    def extraer_productos(self):
        productos = []
        for dicc in self.leer():
            productos.append(Producto.from_dict(dicc))
        return productos

    def escribir_productos(self, productos):
        lista = []
        for prod in productos:
            lista.append(prod.to_dict())
        return self.guardar(lista)

    def definir_id(self):
        productos = self.extraer_productos()
        if not productos:
            return 1
        return max(p.id_producto for p in productos) + 1

    def buscar(self, filtro, valor):
        resultados = []
        for producto in self.extraer_productos():
            if filtro == "nombre":
                if set(producto.nombre.lower().split()) & set(valor.lower().split()):
                    resultados.append(producto)
            elif filtro == "id":
                if producto.id_producto == valor:
                    resultados.append(producto)
            elif filtro == "precio":
                if producto.precio == valor:
                    resultados.append(producto)
        return resultados

    