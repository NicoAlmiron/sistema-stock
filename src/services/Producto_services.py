from src.utils.Helpers import limpiar_consola, pedir_nombre, pedir_precio, pedir_stock, pedir_id
from src.utils.Helpers import cabecera_menu, guion_base, guion_item, pedir_opcion, guion_titulo, pausar_consola
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
        cabecera_menu()
        guion_titulo('PRODUCTO NUEVO')
        id = Gestion_Producto().definir_id()
        guion_titulo()
        guion_item(f'Producto ID: {id}')
        nombre_prod = pedir_nombre(input(f'|{" "*20}+ Nombre del articulo: '))
        precio_prod = pedir_precio(input(f'|{" "*20}+ Precio: $'))
        stock_prod = pedir_stock(input(f'|{" "*20}+ Stock Inicial: '))

        producto = Producto(id_producto = id, nombre= nombre_prod, precio= precio_prod,stock= stock_prod)
        productos = Gestion_Producto().extraer_productos()

        if productos:
            productos.append(producto)
        else:
            productos = []
            productos.append(producto)
        Gestion_Producto().escribir_productos(productos)
        guion_base()
        guion_titulo("Se Guardo el producto exitosamente!")
        pausar_consola()

    except TecStoreError as er:
        pausar_consola(er.mensaje_default)

#   ______________________
#|--| Modificar Producto |-----------------------------------------------------
def mod_prod():
    try:
        productos = Gestion_Producto().extraer_productos()
        
        cabecera_menu()
        guion_titulo('MODIFICAR DATOS DEL PRODUCTO')
        guion_base()
        Gestion_Producto().listar_productos()

        guion_base()
        guion_item('Ingrese el ID del Producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for i , prod in enumerate(productos):
            if prod.id_producto == id_buscar:
                prod.modificar_producto()
                break

        if Gestion_Producto().escribir_productos(productos): 
            pausar_consola("Se Guardo el producto exitosamente!")
        else:
            pausar_consola("Error al guardar el producto")
    except TecStoreError as er:
        pausar_consola(er.mensaje_default)

#   _______________________________
#|--| Modificar Stock de Producto |-----------------------------------------------------
def mod_stock_prod():
    while True:
        try:
            productos = Gestion_Producto().extraer_productos()
            limpiar_consola()
            cabecera_menu()
            guion_titulo('MODIFICAR STOCK DE PRODUCTOS')
            guion_base()
            Gestion_Producto().listar_productos()
            
            guion_base()
            guion_item('Ingrese el ID del Producto')
            id_buscar = pedir_id(input('|##-· ID: '))
            for i , prod in enumerate(productos):
                if prod.id_producto == id_buscar:
                    prod.modificar_stock()    
                    break
            if Gestion_Producto().escribir_productos(productos): 
                pausar_consola("Se actualizo el stock exitosamente!")
            else:
                pausar_consola("Error al guardar el producto")
        except TecStoreError as er:
            pausar_consola(er.mensaje_default)
            break

#   _____________________
#|--| Eliminar Producto |-----------------------------------------------------
def eliminar_producto():
    try:
        productos = Gestion_Producto().extraer_productos()
        limpiar_consola()
        cabecera_menu()
        guion_titulo('DISCONTINUAR PRODUCTOS')
        guion_base()
        Gestion_Producto().listar_productos()
                    
        guion_base()
        guion_item('Ingrese el ID del Producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for prod in productos:
            if prod.id_producto == id_buscar:
                guion_item(f'Producto: {prod.nombre.upper()} - ${prod.precio:,}')
                guion_titulo(f"*Esta seguro que quiere discontinuar este Producto?")
                guion_titulo( 'Confirmar - 1   |    Cancelar - 0')
                opcion = pedir_opcion(input("|#Opcion: "))  
                if opcion == "1":
                    prod.discontinuar_producto()
                    Gestion_Producto().escribir_productos(productos)
                    pausar_consola("Se discontinuo el Producto exitosamente!")
                elif opcion == "0":
                    raise OperacionCancelada()
                else:
                    raise OpcionInvalida()
    except TecStoreError as er:
        pausar_consola(er)
    except ValueError:
        pausar_consola('Ingrese valores Numericos')


#   ____________________
def reactivacion_producto():
    lista_productos = Gestion_Producto().extraer_productos()

    product = [p for p in lista_productos if p.discontinuado]
    #product = list(filter(lambda p: p.discontinuado == True, lista_productos))

    try:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('REACTIVACION DE PRODUCTOS')
        guion_base()
        Gestion_Producto().listar_productos(product, True)
        guion_base()
        guion_item('Ingrese el ID del Producto')
        id_buscar = pedir_id(input('|##-· ID: '))
        for prod in product:
            if prod.id_producto == id_buscar:
                guion_item(f'Producto: {prod.nombre.upper()} - ${prod.precio:,}')
                guion_titulo(f"*Esta seguro que quiere reactivar este Producto?")
                guion_titulo( 'Confirmar - 1   |    Cancelar - 0')
                opcion = input("#Opcion: ")       
                if opcion != "" and opcion.isdigit():
                    if opcion == "0":
                        raise OperacionCancelada()
                    elif opcion == "1":
                        for p in lista_productos:
                            if prod.id_producto == p.id_producto:
                                p.reactivar_producto()
                        Gestion_Producto().escribir_productos(lista_productos)
                        pausar_consola("Se Reactivo el Producto exitosamente!")
                    else:
                        raise OpcionInvalida()
                else:
                    raise OperacionCancelada()
            else:
                pausar_consola("No se encontro el ID del producto!")
    except TecStoreError as er:
        pausar_consola(er.mensaje_default)
    except ValueError:
        pausar_consola('Ingrese valores Numericos')


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





