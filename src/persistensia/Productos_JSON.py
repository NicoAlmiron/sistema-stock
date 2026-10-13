from src.classes import Producto
import json

ARCHIVO_PRODUCTOS_JSON = 'src/data/productos.json'


def extraer_productos(): 

    try:
        productos = [] 
        with open(ARCHIVO_PRODUCTOS_JSON , 'r', encoding='UTF-8') as archivo_producto:
            lista_prod = json.load(archivo_producto)
            if len(lista_prod) <= 0:
                print("Archivo Vacio")
            for prod in lista_prod:
                producto = Producto(
                    id_producto = int(prod["id_producto"]),
                    nombre = prod["nombre"],
                    precio = float(prod["precio"]),
                    cant_vendidos =int(prod["cant_vendidos"]),
                    discontinuado = bool(prod["discontinuado"]),
                    stock = int(prod["stock"]) 
                )
                productos.append(producto)

        
        return productos

    except:
        
        return []


#   __________________________________
#|--| Guardar producto en el archivo |-------------------------------------------------


def escribir_productos(productos):

    lista_productos = []

    for prod in productos:
        lista_productos.append(prod.to_dict())

    try:

        with open(ARCHIVO_PRODUCTOS_JSON, 'w', encoding='UTF-8') as archivo_producto:
            prod_json = json.dumps(
                lista_productos, 
                indent=4)
            archivo_producto.write(prod_json)
        return True
    except FileNotFoundError:
        with open(ARCHIVO_PRODUCTOS_JSON, 'w', encoding='UTF-8') as archivo_producto:
            prod_json = json.dumps(
                lista_productos, 
                indent=4)
            archivo_producto.write(prod_json)
        return True
    except:
        return False






