from src.persistensia import escribir_productos, extraer_productos
from src.utils.Helpers import limpiar_consola, pedir_nombre, pedir_precio, pedir_stock, pedir_id
from src.classes import Producto
from src.exceptions.excepciones import TecStoreError, OperacionCancelada, OpcionInvalida, ArchivoVacio

#------                                           ------#
#--------               PRODUCTOS               --------#
#------                                           ------#
def definir_id():
    productos = extraer_productos()
    if not productos:
        return 1
    return max(p.id_producto for p in productos) + 1


#|--------  PRODUCTOS --------|#
#   ____________________
#|--| Agregar Producto |-----------------------------------------------------
def agregar_prod():

    try:
        print('|###--··  TecStore  ··--###|')
        print('|##-· Producto Nuevo')
        id = definir_id()
        print(f'|##-· Producto ID: {id}')
        nombre_prod = pedir_nombre(input('|-Nobre del articulo: ').lower())
        precio_prod = pedir_precio(input('|-Precio: $'))
        stock_prod = pedir_stock(input('|-Stock Inicial: '))

        producto = Producto(id_producto = id, nombre= nombre_prod, precio= precio_prod,stock= stock_prod)
        productos = extraer_productos()

        if productos:
            productos.append(producto)
        else:
            productos = []
            productos.append(producto)
        escribir_productos(productos)
        print("Se Guardo el producto exitosamente!")

    except TecStoreError as er:
        print(er)

#   ______________________
#|--| Modificar Producto |-----------------------------------------------------
def mod_prod():
    try:
        productos = extraer_productos()
        
        print('|###--··  TecStore  ··--###|')
        listar_productos()


        print('|##-· Ingrese el Id del producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for i , prod in enumerate(productos):
            if prod.id_producto == id_buscar:
                print(f'|##-· Producto ID: {prod.id_producto}')
                try:
                    print(f"|-Nobre anterior *{prod.nombre}*")
                    productos[i].nombre = pedir_nombre(input('|-Nobre del articulo: '))
                except OperacionCancelada:
                    pass
                try:    
                    print(f"|-Precio anterior $*{prod.precio:,}*".replace(",","."))
                    productos[i].precio = pedir_precio(input('|-Precio: $'))
                except OperacionCancelada:
                    pass

                break

        if escribir_productos(productos): 
            print("|· Se Guardo el producto exitosamente!")
        else:
            print("Error al guardar el producto")
    except TecStoreError as er:
        print(er)

#   _______________________________
#|--| Modificar Stock de Producto |-----------------------------------------------------
def mod_stock_prod():
    try:
        productos = extraer_productos()
            
        print('|###--··  TecStore  ··--###|')
        listar_productos()
        print('|##-· Ingrese el Id del producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for i , prod in enumerate(productos):
            if prod.id_producto == id_buscar:
                print(f'|##-· Producto ID: {prod.id_producto}')
                try:
                    print(f"| {prod.nombre}*")
                    print(f"| -Stock actual *{prod.stock}*")
                    productos[i].stock = pedir_stock(input('|-Nuevo Stock: '))
                except OperacionCancelada:
                    pass
    
                break
    
        if escribir_productos(productos): 
            print("|· Se actualizo el stock exitosamente!")
        else:
            print("Error al guardar el producto")
    except TecStoreError as er:
        print(er)

#   _____________________
#|--| Eliminar Producto |-----------------------------------------------------
def eliminar_producto():
    productos = extraer_productos()
    try:
        print('|###--··  TecStore  ··--###|')
        print('|##-· Ingrese el Id del producto')
        listar_productos()
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
                        escribir_productos(productos)
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
#|--| Listar Productos |-----------------------------------------------------
def listar_productos(lista_productos = None):
    if lista_productos is None:
        lista_productos = extraer_productos()

    if lista_productos:
        for i, producto in enumerate(lista_productos):
            print(producto)
        #input('|· precione una tecla para continuar')
    else:
        raise ArchivoVacio()
        
#   ________________________________
#|--| Mostrar un producto por 'id' |-----------------------------------------------------
def mostrar_un_prod(id):
    productos = extraer_productos()
    encontrado = False
    for producto in productos:
        if producto.id_producto == id:
            encontrado = True
            return producto
    if encontrado is False : return False



#   ____________________
#|--| Descontar Stock  |-----------------------------------------------------
def descontar_stock(lista_prods ,id ,cantidad):
    for i, producto in enumerate(lista_prods):
        if producto.id_producto == id:
            lista_prods[i].stock = producto.stock - cantidad

    return lista_prods



#   ______________________
#|--| Filtrar Productos  |-----------------------------------------------------
def fitrador(filtro, buscar, lista_prod):
    productos = lista_prod.__dict__
    encontrado = False
    for producto in productos:
        for clave, valor in producto.items():
            if clave == filtro and valor == buscar:
                encontrado = True
                return mostrar_un_prod(int(producto['id']))
    if encontrado == False:
        print('|#·No se econtro el producto!***')


#   __________________________
#|--| Buscardor de Productos |-----------------------------------------------------
def buscador(productos):
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
                nombre = input('|Nombre···---: ').lower()
                prod = fitrador('nombre', nombre.lower())
                if prod :
                    print(prod)
                else:
                    print('# *No se encontro el producto***')
            case "2":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el ID a Buscar')
                id_prod = int(input('|ID ···---: '))
                prod = fitrador('id', id_prod)
                if prod :
                    print(prod)
                else:
                    print('# *No se encontro el producto***')
            case "3":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Precio a Buscar')
                precio = float(input('|Precio ···---: $'))
                prod = fitrador('precio', precio)
                if prod :
                    print(prod)
                else:
                    print('# *No se encontro el producto***')
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')
        
        input('precione una tecla para continuar!')


