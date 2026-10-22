from src.model import Producto
from src.exceptions.excepciones import ArchivoVacio
import json

class Gestion_Producto():
    def __init__(self):
        self.arch_json = 'src/data/productos.json'

    def extraer_productos(self): 

        try:
            productos = [] 
            with open(self.arch_json , 'r', encoding='UTF-8') as archivo_producto:
                lista_prod = json.load(archivo_producto)
                if not lista_prod:
                    return []
                for prod in lista_prod:
                    producto = Producto.from_dict(prod)
                    productos.append(producto)
            return productos
        except FileNotFoundError:
            return []
        except:
            return []

    #   __________________________________
    #|--| Guardar producto en el archivo |-------------------------------------------------

    def escribir_productos(self, productos):

        lista_productos = []

        for prod in productos:
            lista_productos.append(prod.to_dict())

        try:

            with open(self.arch_json, 'w', encoding='UTF-8') as archivo_producto:
                prod_json = json.dumps(
                    lista_productos, 
                    indent=4)
                archivo_producto.write(prod_json)
            return True
        except FileNotFoundError:
            with open(self.arch_json, 'w', encoding='UTF-8') as archivo_producto:
                prod_json = json.dumps(
                    lista_productos, 
                    indent=4)
                archivo_producto.write(prod_json)
            return True
        except:
            return False

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
        productos = Gestion_Producto.extraer_productos()
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
            raise ArchivoVacio('|· No se encontraron coincidencias')
