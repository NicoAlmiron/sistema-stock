from src.utils.Helpers import (limpiar_consola, pedir_nombre, pedir_precio, pedir_stock, pedir_id, guion_opcion,
                               cabecera_menu, guion_base, guion_item, pedir_opcion, guion_titulo, pausar_consola)
from src.model import Producto
from src.exceptions.excepciones import (TecStoreError, OperacionCancelada, OpcionInvalida, IdNoEncontrado, ArchivoVacio)
from src.persistensia.Gestion_Producto import Gestion_Producto

#------                                           ------#
#--------               PRODUCTOS               --------#
#------                                           ------#

#|--------  PRODUCTOS --------|#
#   ____________________
#|--| Mostrar Productos |-----------------------------------------------------
def listar_productos(lista_productos=None, mostrar_discontinuados=False):
    if lista_productos is None:
        lista_productos = Gestion_Producto().extraer_productos()

    if not lista_productos:
        raise ArchivoVacio()
    for producto in lista_productos:
        if mostrar_discontinuados or not producto.discontinuado:
            print(producto)


def mostrar_busqueda(filtro, valor):
    resultados = Gestion_Producto().buscar(filtro, valor)
    if not resultados:
        raise ArchivoVacio('No se encontraron coincidencias')
    for producto in resultados:
        print(producto)

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
        pausar_consola(er.mensaje)

#   ______________________
#|--| Modificar Producto |-----------------------------------------------------
def mod_prod():
    try:
        productos = Gestion_Producto().extraer_productos()
        
        cabecera_menu()
        guion_titulo('MODIFICAR DATOS DEL PRODUCTO')
        guion_base()
        listar_productos()

        guion_base()
        guion_item('Ingrese el ID del Producto')
        id_buscar = pedir_id(input('|##-· ID: '))

        prod = next((p for p in productos if p.id_producto == id_buscar), None)

        if prod is None:
            raise IdNoEncontrado()
        print(f'|##-· Producto ID: {prod.id_producto}')
        try:
            print(f"|-Nombre anterior *{prod.nombre}*")
            prod.nombre = pedir_nombre(input('|-Nombre del articulo: '))
        except OperacionCancelada:
            pass
        try:
            print(f"|-Precio anterior $*{prod.precio:,}*".replace(",", "."))
            prod.precio = pedir_precio(input('|-Precio: $'))
        except OperacionCancelada:
            pass

        if Gestion_Producto().escribir_productos(productos): 
            pausar_consola("Se Guardo el producto exitosamente!")
        else:
            raise TecStoreError()
    except TecStoreError as er:
        pausar_consola(er.mensaje)



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
            listar_productos()
            
            guion_base()
            guion_item('Ingrese el ID del Producto')
            id_buscar = pedir_id(input('|##-· ID: '))

            prod = next((p for p in productos if p.id_producto == id_buscar), None)
            if prod is None:
                raise IdNoEncontrado()
            print(f'|##-· Producto ID: {prod.id_producto}')
            print(f"| {prod.nombre}")
            print(f"| -Stock actual *{prod.stock}*")
            try:
                prod.stock = pedir_stock(input('|-Nuevo Stock: '))
            except OperacionCancelada:
                pass
            
            if Gestion_Producto().escribir_productos(productos): 
                pausar_consola("Se actualizo el stock exitosamente!")
            else:
                raise TecStoreError()
        except TecStoreError as er:
            pausar_consola(er.mensaje)
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
        listar_productos()
                    
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
        pausar_consola(er.mensaje)


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
        listar_productos(product, True)
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
                raise IdNoEncontrado()
    except TecStoreError as er:
        pausar_consola(er.mensaje)



#|--| Descontar Stock  |-----------------------------------------------------
def descontar_stock(lista_prods ,id ,cantidad):
    for i, producto in enumerate(lista_prods):
        if producto.id_producto == id:
            producto.descontar_stock(cantidad)
    return lista_prods



#   __________________________
#|--| Buscardor de Productos |-----------------------------------------------------
def buscador():
    productos = Gestion_Producto().extraer_productos()
    try:
        while True:
            limpiar_consola()
            cabecera_menu()
            guion_titulo('BUSCADOR DE PRODUCTOS')
            guion_titulo('')
            if len(productos) == 0:
                pausar_consola('No se encontraron productos!')
                return
            guion_opcion("1","Buscar por Nombre")
            guion_opcion("2","Buscar por ID")
            guion_opcion("3","Buscar por Precio")
            guion_opcion("0","Salir")
            op = input(f'|{" "*30}OPCION···---: ')
    
            match op:
                case "1":
                    limpiar_consola()
                    cabecera_menu()
                    guion_titulo('BUSCADOR DE PRODUCTOS')
                    guion_titulo('')
                    guion_item('Ingrese el Nombre del producto a Buscar')
                    guion_titulo('')
                    nombre = pedir_nombre(input(f'|{" "*25}·Nombre···---: ')).lower()
                    guion_titulo('')
                    mostrar_busqueda('nombre', nombre.lower())
                    guion_titulo('')
                case "2":
                    limpiar_consola()
                    cabecera_menu()
                    guion_titulo('BUSCADOR DE PRODUCTOS')
                    guion_titulo('')
                    guion_item('Ingrese el ID del producto a Buscar')
                    id_prod = pedir_id(input(f'|{" "*30}·ID ···---: '))
                    mostrar_busqueda('id', id_prod)
                case "3":
                    limpiar_consola()
                    cabecera_menu()
                    guion_titulo('BUSCADOR DE PRODUCTOS')
                    guion_titulo('')
                    guion_item('Ingrese el Precio del producto a Buscar')
                    precio = pedir_precio(input(f'|{" "*30}·Precio ···---: $'))
                    mostrar_busqueda('precio', precio)
                case "0":
                    break
                case _:
                    raise OpcionInvalida()
            
            pausar_consola()
    except TecStoreError as er:
        pausar_consola(er.mensaje)