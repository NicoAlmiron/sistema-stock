from src.utils.Helpers import limpiar_consola, pedir_nombre, pedir_precio, pedir_stock, pedir_id
from src.model import Producto
from src.exceptions.excepciones import TecStoreError, OperacionCancelada, OpcionInvalida
from src.persistensia.Gestion_Producto import Gestion_Producto

#------                                           ------#
#--------               PRODUCTOS               --------#
#------                                           ------#

#|--------  PRODUCTOS --------|#
#   ____________________
#|--| Agregar Producto |-----------------------------------------------------
def agregar_prod():

    try:
        print('|###--··  TecStore  ··--###|')
        print('|##-· Producto Nuevo')
        id = Gestion_Producto().definir_id()
        print(f'|##-· Producto ID: {id}')
        nombre_prod = pedir_nombre(input('|-Nobre del articulo: ').lower())
        precio_prod = pedir_precio(input('|-Precio: $'))
        stock_prod = pedir_stock(input('|-Stock Inicial: '))

        producto = Producto(id_producto = id, nombre= nombre_prod, precio= precio_prod,stock= stock_prod)
        productos = Gestion_Producto().extraer_productos()

        if productos:
            productos.append(producto)
        else:
            productos = []
            productos.append(producto)
        Gestion_Producto().escribir_productos(productos)
        print("Se Guardo el producto exitosamente!")

    except TecStoreError as er:
        print(er)

#   ______________________
#|--| Modificar Producto |-----------------------------------------------------
def mod_prod():
    try:
        productos = Gestion_Producto().extraer_productos()
        
        print('|###--··  TecStore  ··--###|')
        Gestion_Producto().listar_productos()


        print('|##-· Ingrese el Id del producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for i , prod in enumerate(productos):
            if prod.id_producto == id_buscar:
                prod.modificar_producto()
                break

        if Gestion_Producto().escribir_productos(productos): 
            print("|· Se Guardo el producto exitosamente!")
        else:
            print("Error al guardar el producto")
    except TecStoreError as er:
        print(er)

#   _______________________________
#|--| Modificar Stock de Producto |-----------------------------------------------------
def mod_stock_prod():
    try:
        productos = Gestion_Producto().extraer_productos()
            
        print('|###--··  TecStore  ··--###|')
        Gestion_Producto().listar_productos()
        print('|##-· Ingrese el Id del producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for i , prod in enumerate(productos):
            if prod.id_producto == id_buscar:
                prod.modificar_stock()    
                break
        if Gestion_Producto().escribir_productos(productos): 
            print("|· Se actualizo el stock exitosamente!")
        else:
            print("Error al guardar el producto")
    except TecStoreError as er:
        print(er)

#   _____________________
#|--| Eliminar Producto |-----------------------------------------------------
def eliminar_producto():
    productos = Gestion_Producto().extraer_productos()
    try:
        print('|###--··  TecStore  ··--###|')
        print('|##-· Ingrese el Id del producto')
        Gestion_Producto().listar_productos()
        id_buscar = pedir_id(input('|##-· ID: '))
        for prod in productos:
            if prod.id_producto == id_buscar:
                print(f"\n# Producto: {prod.nombre.upper()} - ${prod.precio:,}\n")
                print(f"# *Esta seguro que quiere eliminar este Producto?")
                print( '#     Confirmar - 1   |    Cancelar - 0')
                opcion = input("#Opcion: ")       
                if opcion != "" and opcion.isdigit():
                    if opcion == "0":
                        raise OperacionCancelada()
                    elif opcion == "1":
                        productos.remove(prod)
                        Gestion_Producto().escribir_productos(productos)
                        print("Se Elimino el Producto exitosamente!")
                    else:
                        raise OpcionInvalida()
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        input(er)
    except ValueError:
        input('|· Ingrese valores Numericos')

#   ____________________
#|--| Descontar Stock  |-----------------------------------------------------
def descontar_stock(lista_prods ,id ,cantidad):
    for i, producto in enumerate(lista_prods):
        if producto.id_producto == id:
            producto.desc_stock(cantidad)
    return lista_prods



#   __________________________
#|--| Buscardor de Productos |-----------------------------------------------------
def buscador():
    productos = Gestion_Producto().extraer_productos()
    while True:
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        print('|##······················##|')
        if len(productos) == 0:
            print('|\t·No se emcontraron productos!')
            return
        print('| 1 ) --- Buscar por Nombre')
        print('| 2 ) --- Buscar por ID')
        print('| 3 ) --- Buscar por Precio')
        print('| 0 ) --- Salir')
        op = input('|OPCION···---: ')

        limpiar_consola()
        match op:
            case "1":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Nombre a Buscar')
                nombre = pedir_nombre(input('|Nombre···---: ')).lower()
                Gestion_Producto().fitrador('nombre', nombre.lower())
            case "2":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el ID a Buscar')
                id_prod = pedir_id(input('|ID ···---: '))
                Gestion_Producto().fitrador('id', id_prod)
            case "3":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Precio a Buscar')
                precio = pedir_precio(input('|Precio ···---: $'))
                Gestion_Producto().fitrador('precio', precio)
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')
        
        input('precione una tecla para continuar!')


def reactivacion_producto():
    lista_productos = Gestion_Producto().extraer_productos()

    productos = list(filter(lambda p: p == True, lista_productos))

    try:
        print('|###--··  TecStore  ··--###|')
        print('|##-· Ingrese el Id del producto')
        Gestion_Producto().listar_productos()
        id_buscar = pedir_id(input('|##-· ID: '))
        for prod in productos:
            if prod.id_producto == id_buscar:
                print(f"\n# Producto: {prod.nombre.upper()} - ${prod.precio:,}\n")
                print(f"# *Esta seguro que quiere reactivar este Producto?")
                print( '#     Confirmar - 1   |    Cancelar - 0')
                opcion = input("#Opcion: ")       
                if opcion != "" and opcion.isdigit():
                    if opcion == "0":
                        raise OperacionCancelada()
                    elif opcion == "1":
                        productos.remove(prod)
                        Gestion_Producto().escribir_productos(productos)
                        print("Se Reactivo el Producto exitosamente!")
                    else:
                        raise OpcionInvalida()
                else:
                    raise OperacionCancelada()
    except TecStoreError as er:
        input(er)
    except ValueError:
        input('|· Ingrese valores Numericos')

