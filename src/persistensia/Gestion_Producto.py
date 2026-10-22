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

    def listar_productos(self, lista_productos = None, mostrar_discontinuados=False):
        if lista_productos is None:
            lista_productos = self.extraer_productos()

        if lista_productos:
            for producto in lista_productos:
                if mostrar_discontinuados or not producto.discontinuado:
                    print(producto)
        else:
            raise ArchivoVacio()

    def mostrar_un_prod(self, id):
        productos = self.extraer_productos()
        encontrado = False
        for producto in productos:
            if producto.id_producto == id:
                encontrado = True
                return producto
        if not encontrado : return False

    def fitrador(self, filtro, buscar):
        productos = Gestion_Producto().extraer_productos()
        encontrado = False
        resultados = []
        for producto in productos:

            if filtro == "nombre":
                if bool(set(producto.nombre.lower().split()) & set(buscar.lower().split())):
                    encontrado = True
                    print(producto)

            if filtro == "id":
                if producto.id_producto == buscar:
                    encontrado = True
                    print(producto)
            
            if filtro == "precio":
                if producto.precio == buscar:
                    encontrado = True
                    print(producto)
        if encontrado == False:
            raise ArchivoVacio('No se encontraron coincidencias')