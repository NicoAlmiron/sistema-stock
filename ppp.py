from utils.Helpers import limpiar_consola



#------                                           ------#
#--------               PRODUCTOS               --------#
#------                                           ------#


#- Diccionarios de datos
#Producto: 
#      "id" - entero - 6 bits
#  "nombre" - string - 30 bits
#  "precio" - flotante - 11 bits - (99999999.99)
#   "stock" - entero - 4 bits

# Registro de referencia:
#1     |cosme fulanito               |25000.00   |20  |     


producto = {
    #"id": 1,
    #"nombre": "teclado mecanico",
    #"precio": 150000,
    #"stock": 8
}

productos = [
    # {
    #     "id": 1,
    #     "nombre": "teclado mecanico",
    #     "precio": 150000,
    #     "stock": 8
    # },
    # {
    #     "id": 2,
    #     "nombre": "mouse gamer RGB",
    #     "precio": 50000,
    #     "stock": 9
    # },
    # {
    #     "id": 3,
    #     "nombre": "prueba",
    #     "precio": 90000,
    #     "stock": 10
    # }
]


#--                                                   --#
#----                                               ----#
#------                                           ------#
#--------  Funciones para gestion de archivos   --------#
#------                                           ------#
#----                                               ----#
#--                                                   --#



#|--------  ARCHIVO PRODUCTO   --------|#
#   ________________________________
#|--| Extraer productos del archivo|-----------------------------------------------------

def extraer_productos():   

    #  Abre con la funcion integrada -with open- el archivo "Productos.txt"
    #  en modo 'r' (read / leer), se extraen todas las lineas (cada linea
    #  es un registro) y se las agrega en una lista 'registros' luego,
    #  recorre los registros ('reg'), crea una instancia del diccionario 
    #  'producto' e inicializa las claves con las secciones que le corresponde,
    #  casteando los atributos que son numeros y a los atributos que son tipo
    #  -string- les quita los espacios con la funcion -strip-, cuando termina
    #  de guardar todo en el diccionario, procede a agregarlo en la lista 'productos'
    #  la cual sera usada en todo el programa

    registros = []

    with open('Productos.txt', 'r', encoding='UTF-8') as archivo_producto:
        registros = archivo_producto.readlines()
        if len(registros) <= 0:
            return
        for reg in registros:
            producto ={
                "id": int(reg[0:6]),
                "nombre": reg[7:36].strip('  '),
                "precio": float(reg[38:48]),
                "stock": int(reg[50:53]),
                }
            productos.append(producto)



#   __________________________________
#|--| Guardar producto en el archivo |-------------------------------------------------

def escribir_producto(producto):

    #  Recibe de parametro un diccionario que se llama 'producto', luego con la funcion 
    #  -with open- abre el archivo "Productos.txt" en modo 'a' ( add / agregar) se crea
    #  una variable tipo -string- llamada 'reg_prod', se inicializa en vacio (""), esta
    #  contendra el registro con el formato correcto (listo para ser guardado), por cada
    #  atributo del 'producto' se corrobora la longitud, si la longitud no llega al limite 
    #  dispuesto, se completa con espacios en blanco, ademas se agrega un separador '|' 
    #  y se suma al final de la cadena, cuando se completa la cadena con los datos, 
    #  se procede a escribir la variable 'reg_prod' con el metodo -write- en el archivo 
    #  'archivo_producto', este registro se escribe al final del archivo
    

    with open('Productos.txt', 'a', encoding='UTF-8') as archivo_producto:
        reg_prod = ""
        reg_prod += f"{producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}|" # id producto
        reg_prod += f"{producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}|" # nombre
        reg_prod += f"{producto['precio']}{(" " * ( 11 - len(str(producto['precio'])) ) )}|" # precio
        reg_prod += f"{producto['stock']}{(" " * ( 4 - len(str(producto['stock'])) ) )}|\n" # stock
        archivo_producto.write(reg_prod)



#   _____________________________________________
#|--| Borra todo y reescrive todo en el archivo |-------------------------------------------------

def reescribir_productos_archivo():

    #  Abre con la funcion integrada -with open- el archivo "Productos.txt"
    #  en modo 'w' (write / escribir), este metodo borra todo el archivo, luego recorre 
    #  la lista 'productos'. Por cada iteracion se crea una variable tipo -string- 
    #  llamada 'reg_prod', se inicializa en vacio (""), esta contendra el registro con 
    #  el formato correcto (listo para ser guardado), por cada atributo del 'producto' 
    #  se corrobora la longitud, si la longitud no llega al limite dispuesto, se completa 
    #  con espacios en blanco, ademas se agrega un separador '|' y se suma al final de 
    #  la cadena, cuando se completa la cadena con los datos, se procede a escribir la 
    #  variable 'reg_prod' con el metodo -write- en el archivo 'archivo_producto',
    #  estos registros se van escribiendo al final del archivo, uno despues del otro

    with open('Productos.txt', 'w', encoding='UTF-8') as archivo_producto:
        for producto in productos:
            reg_prod = ""
            reg_prod += f"{producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}|" # id producto
            reg_prod += f"{producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}|" # nombre
            reg_prod += f"{producto['precio']}{(" " * ( 11 - len(str(producto['precio'])) ) )}|" # precio
            reg_prod += f"{producto['stock']}{(" " * ( 4 - len(str(producto['stock'])) ) )}|\n" # stock
            archivo_producto.write(reg_prod)



#------                                           ------#
#--------                  VENTA                --------#
#------                                           ------#


# primer intento de diccionario (funcionaba en la primer vercion)
# ventas = [
#     {
#         "id_venta": 1,
#         "detalle_venta": {
#             1 : (2, 300000),
#             2 : (1, 50000)
#         },
#         "importe_total": 350000,
#         "forma_pago": 'Efectivo'
#     },
#     {
#         "id_venta": 2,
#         "detalle_venta": {
#             2 : (1, 50000)
#         },
#         "importe_total": 50000,
#         "forma_pago": 'Tarjeta'
#     },
# ]




#- Diccionarios de datos
# Venta:
#       "id_venta" - entero - 10 bits
#  "importe_total" - flotante (999,999,999.9) - 11 bits
#     "forma_pago" - string - 13 bits

# Registro de referencia:
#1         |500000.0   |Transferencia|
 

# Detalles_Ventas
#      "id_venta" - entero - 6 bits
#   "id_producto" - entero - 6 bits
#      "cantidad" - entero - 3 bits
#      "subtotal" - flotante (99999999.99) - 11 bits

# Registro de referencia:
#1     |2     |2  |300000.0   |

venta = {
    #"id_venta": 1,
    #"detalle_venta": [
    #{
    #    'id_producto' : 1,
    #    'detalle_prod' : 
    #    {
    #        'cantidad': 2,
    #        'sub_total': 300000       
    #    },
    #},
    #{
    #    'id_producto' : 2,
    #    'detalle_prod' :
    #    {
    #        'cantidad': 1,
    #        'sub_total': 50000                
    #    },
    #}],
    #"importe_total": 350000,
    #"forma_pago": 'Efectivo',
}

detalle_venta = {
    #'id_producto' : 1,
    #'detalle_prod' : 
    #{
    #    'cantidad': 2,
    #    'sub_total': 300000       
    #},
}

ventas = [
    # {
    #     "id_venta": 1,
    #     "detalle_venta": [
    #     {
    #         'id_producto' : 1,
    #         'detalle_prod' : 
    #         {
    #             'cantidad': 2,
    #             'sub_total': 300000       
    #         },
    #     },
    #     {
    #         'id_producto' : 2,
    #         'detalle_prod' :
    #         {
    #             'cantidad': 1,
    #             'sub_total': 50000                
    #         },
    #     }],
    #     "importe_total": 350000,
    #     "forma_pago": 'Efectivo',
    # },
    # {
    #     "id_venta": 2,
    #     "detalle_venta": [{
    #         'id_producto': 1,
    #         'detalle_prod':
    #         {
    #                'cantidad': 1,
    #                'sub_total': 50  
    #         }              
    #        }],
    #     "importe_total": 50000,
    #     "forma_pago": 'Tarjeta'
    # },
]





#|--------  ARCHIVO VENTA   --------|#
#   _____________________________
#|--| Extraer ventas del archivo|-----------------------------------------------------

def extraer_ventas():

    #  Abre con la funcion integrada -with open- ambos archivos "venta.txt" y 
    #  "detalles_ventas.txt" en modo 'r' (read / leer), se extraen todas las
    #  lineas del archivo venta y detalles_ventas se las agrega en las lista
    #  'ventas_arch' y 'detalles_ventas', luego recorre la lista 'ventas_arch', 
    #  en cada 'venta_item', se crea una instacia de un diccionario 'venta', en
    #  el cual, se inicializa las claves con los valores que contenian cada
    #  seccion del 'venta_item', luego recorre la lista 'detalles_ventas', donde
    #  por cada item ('det_vent') que recorre pregunta si es que en los 6 primeros
    #  caracteres, son el id de la venta que se esta guardando, si encuentra
    #  coincidencia, se crea una instacia de un diccionario 'detalle_venta', en 
    #  el cual, se inicializa las claves con los valores que contenian cada
    #  seccion del item ('det_vent') y guarda este diccionacio en la clave 
    #  "detalle_venta" del dicionario 'venta'. Cuando ya guardo todos los
    #  detalles, recien guarda la venta en la lista 'ventas' que se usara
    #  en todo el programa. 

    ventas_arch = []
    detalles_ventas = []

    with open('venta.txt', 'r', encoding='UTF-8') as arch_venta, open('detalles_ventas.txt', 'r', encoding='UTF-8') as arch_detalle_venta:
        ventas_arch = arch_venta.readlines()
        detalles_ventas = arch_detalle_venta.readlines()
        if len(ventas_arch) <= 0:
            return 
        for venta_item in ventas_arch:
            venta ={
                "id_venta": int(venta_item[0:9]),
                "detalle_venta": [],
                "importe_total": float(venta_item[11:21]),
                "forma_pago": venta_item[23:36].strip('  ')
                }
            
            
            for det_vent in detalles_ventas:
                if int(det_vent[0:5]) == venta['id_venta']:
                    #print(f"{int(det_vent[0:5])} -  {venta['id_venta']}")
                    detalle_venta = {
                        'id_producto': int(det_vent[11:17]),
                        'detalle_prod':
                        {
                               'cantidad': int(det_vent[18:21]),
                               'sub_total': float(det_vent[22:32])  
                        }              
                    }
                    venta['detalle_venta'].append(detalle_venta)
                    
            ventas.append(venta)



#   _____________________________
#|--| Guardar ventas del archivo|-----------------------------------------------------

def escribir_venta(venta):

    #  Recibe de parametro un diccionario 'venta', luego abre con la funcion
    #  integrada with open ambos archivos "venta.txt" y "detalles_ventas.txt"
    #  en modo 'a' (write / escribir (se escribe al final del archivo)) se crea
    #  una variable 'reg_vent' tipo string que contendra el registro con el formato 
    #  para ser guardado, por cada atributo se corrobora su longitud, si la longitud
    #  no llega al limite dispuesto se completa con espacios en blanco, cuando se
    #  completa toda la cadena, se procede a escribirse al final del archivo 'arch_venta',
    #  luego por cada detalle de venta que este relacionado a ese 'id_venta' se crea
    #  una variable 'reg_det_vent' tipo string que contendra el registro, por cada
    #  atributo se corrobora su longitud, si la longitud no llega al limite dispuesto
    #  se completa con espacios en blanco, luego, siguiendo el mismo sistema, lo agrega
    #  al final del archivo 'arch_detalle_venta'

    with open('venta.txt', 'a', encoding='UTF-8') as arch_venta, open('detalles_ventas.txt', 'a', encoding='UTF-8') as arch_detalle_venta:
        reg_vent = ""
        reg_vent += f"{venta['id_venta']}{(" " * ( 10 - len(str(venta['id_venta'])) ) )}|" # id venta
        reg_vent += f"{venta['importe_total']}{(" " * ( 11 - len(str(venta['importe_total'])) ) )}|" # nombre
        reg_vent += f"{venta['forma_pago']}{(" " * ( 13 - len(venta['forma_pago']) ) )}|\n"# precio
        arch_venta.write(reg_vent)
        for det_venta in venta['detalle_venta']:
            reg_det_vent = ""
            reg_det_vent += f"{venta['id_venta']}{(" " * ( 10 - len(str(venta['id_venta'])) ) )}|" # id venta
            reg_det_vent += f"{det_venta['id_producto']}{(" " * ( 6 - len(str(det_venta['id_producto'])) ) )}|" # id producto
            reg_det_vent += f"{det_venta['detalle_prod']['cantidad']}{(" " * ( 3 - len(str(det_venta['detalle_prod']['cantidad'])) ) )}|" # cantidad
            reg_det_vent += f"{det_venta['detalle_prod']['sub_total']}{(" " * ( 11 - len(str(det_venta['detalle_prod']['sub_total'])) ) )}|\n" # subtotal
            arch_detalle_venta.write(reg_det_vent)


metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")



#--                                              --#
#----                                          ----#
#------                                      ------#
#--------      Funciones para gestion      --------#
#------                                      ------#
#----                                          ----#
#--                                              --#


#|--------  PRODUCTOS --------|#
#   ____________________
#|--| Agregar Producto |-----------------------------------------------------
def agregar_prod():

    producto = {}
    print('|###--··  TecStore  ··--###|')
    print('|##-· Producto Nuevo')

    ultima_pocicion =  len(productos)-1
    producto['id'] = productos[ultima_pocicion]['id'] + 1
    print(f'|##-· Producto ID: {producto['id']}')

    nombre_prod = input('|-Nobre del articulo: ').lower()
    if nombre_prod == "":
        print("# **Se Cancelo La operacion**")   
        input('precione una tecla para continuar!') 
        return        
    elif len(nombre_prod) > 30:
        print("# **Se exedio el limite de caracteres**")  
        input('precione una tecla para continuar!') 
        return        
    else:
        producto['nombre'] = nombre_prod

    

    precio_prod = input('|-Precio: $')
    if precio_prod == "":
        print("# **Se Cancelo La operacion**")   
        input('precione una tecla para continuar!') 
        return 
    elif len(precio_prod) >= 12:
        print("# **Numero demaciado grande**")   
        input('precione una tecla para continuar!') 
        return 
    elif float(precio_prod) < 0:
        print("# **no puede tener precio menor a cero**")   
        input('precione una tecla para continuar!') 
        return  
    else:
        producto['precio'] = float(precio_prod)


    stock_prod = input('|-Stock Inicial: ')
    if stock_prod == "":
        print("# **Se Cancelo La operacion**")   
        input('precione una tecla para continuar!') 
        return 
    elif len(stock_prod) >= 4:
        print("# **Numero demaciado grande**")   
        input('precione una tecla para continuar!') 
        return 
    elif int(stock_prod) < 0:
        print("# **no puede tener stock menor a cero**")   
        input('precione una tecla para continuar!') 
        return  
    else:
        producto['stock'] = int(stock_prod)


    productos.append(producto)
    escribir_producto(producto)
    print("Se Guardo el producto exitosamente!")


#   ______________________
#|--| Modificar Producto |-----------------------------------------------------
def mod_prod():
    producto = {}
    print('|###--··  TecStore  ··--###|')
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for prod in productos:
        for clave, valor in prod.items():
            if clave == 'id' and int(id_buscar) == valor:      
                print(f'|##-· Producto ID: {prod['id']}')


                print(f"|-Nobre anterior *{prod['nombre']}*")
                nombre_nuevo = input('|-Nobre del articulo: ')
                if len(nombre_nuevo) > 30:
                    print("# **Se exedio el limite de caracteres**")  
                    input('precione una tecla para continuar!') 
                    return        
                elif nombre_nuevo != "":
                    producto['nombre'] = nombre_nuevo

                print(f"|-Precio anterior $*{prod['precio']:,}*".replace(",","."))
                precio_nuevo = input('|-Precio: $')
                if precio_nuevo != "":
                    if len(precio_nuevo) >= 12:
                        print("# **Numero demaciado grande**")   
                        input('precione una tecla para continuar!') 
                        return 
                    elif float(precio_nuevo) < 0:
                        print("# **no puede tener precio menor a cero**")   
                        input('precione una tecla para continuar!') 
                        return  
                    else:
                        producto['precio'] = float(precio_nuevo)

                prod.update(producto)
    reescribir_productos_archivo()
    print("Se Guardo el producto exitosamente!")


#   _______________________________
#|--| Modificar Stock de Producto |-----------------------------------------------------
def mod_stock_prod():
    print('|###--··  TecStore  ··--###|')
    listar_productos(productos)
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for prod in productos:
        for clave, valor in prod.items():
            if clave == 'id' and int(id_buscar) == valor:   
                print(f"| {prod['nombre']}*")
                print(f"| -Stock actual *{prod['stock']}*")
                stock_nuevo = input('|-Nuevo Stock: ')
                if stock_nuevo == "":
                    print("# **Se Cancelo La operacion**")   
                    input('precione una tecla para continuar!') 
                    return 
                elif len(stock_nuevo) >= 4:
                    print("# **Numero demaciado grande**")   
                    input('precione una tecla para continuar!') 
                    return 
                elif int(stock_nuevo) < 0:
                    print("# **no puede tener stock menor a cero**")   
                    input('precione una tecla para continuar!') 
                    return  
                else:
                    prod.update({'stock': int(stock_nuevo)})

    reescribir_productos_archivo()
    print("Se actualizo el stock exitosamente!")

#   _____________________
#|--| Eliminar Producto |-----------------------------------------------------
def eliminar_producto():
    print('|###--··  TecStore  ··--###|')
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for prod in productos:
        for clave, valor in prod.items():
            if clave == 'id' and valor == int(id_buscar):
                print(f"\n# Producto: {prod['nombre'].upper()} - ${prod['precio']:,}\n")
                print(f"# *Esta seguro que quiere eliminar este Producto?")
                print( '#     Confirmar - 1   |    Cancelar - 0')
                opcion = input("#Opcion: ")       
                if opcion != "":
                    if opcion == "0":
                        print("#   **Se Cancelo la operacion!**")                    
                    elif opcion == "1":
                        productos.remove(prod)
                        print("Se Elimino el Producto exitosamente!")
                        reescribir_productos_archivo()
                    else:
                        print("#   **Se Cancelo la operacion!**")
                else:
                    print("#   **Se Cancelo la operacion!**")


#   _________________________________
#|--| Sub-Menu de gestion Productos |-----------------------------------------------------
def abm_producto():
    while True:
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        print('|##······················##|')
        print('| 1 ) --- Agregar Nuevo')
        print('| 2 ) --- Modificar Existente')
        print('| 3 ) --- Modificar Stock')
        print('| 4 ) --- Eliminar')
        print('| 0 ) --- Salir')
        op = input('|OPCION···---: ')

        limpiar_consola()
        match op:
            case "1":
                agregar_prod()
            case "2":
                mod_prod()
            case "3":
                mod_stock_prod()
            case "4":
                eliminar_producto()
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')

        input('precione una tecla para continuar!')


#   ____________________
#|--| Listar Productos |-----------------------------------------------------
def listar_productos(lista_productos):
    if len(lista_productos) == 0:
        print('|\t·No se emcontraron productos!')
        return
    for producto in lista_productos:
        precio_prod = f'{producto['precio']:,}'
        renglon = f'|ID: {producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}'
        renglon += f'| {producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}'
        renglon += f'| ${producto['precio']:,}{(" " * ( 13 - len(precio_prod)))}'
        renglon += f'| STOCK: {producto['stock']}'
        if int(producto['stock']) < 4 and int(producto['stock']) > 0:
            renglon += ' (STOCK BAJO)'
        elif int(producto['stock']) == 0:
            renglon += ' (SIN STOCK!!*!*!*!)'
        print(renglon)

def imprimir_producto(producto):
    precio_prod = f'{producto['precio']:,}'
    renglon = f'|ID: {producto['id']}{(" " * ( 6 - len(str(producto['id'])) ) )}'
    renglon += f'| {producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}'
    renglon += f'| ${producto['precio']:,}{(" " * ( 13 - len(precio_prod)))}'
    renglon += f'| STOCK: {producto['stock']}'
    if int(producto['stock']) < 4 and int(producto['stock']) > 0:
        renglon += ' (STOCK BAJO)'
    elif int(producto['stock']) == 0:
        renglon += ' (SIN STOCK!!*!*!*!)'
    print(renglon)

#   ________________________________
#|--| Mostrar un producto por 'id' |-----------------------------------------------------
def mostrar_un_prod(id):
    encontrado = False
    for producto in productos:
        if producto['id'] == id:
            encontrado = True
            return producto
    if encontrado is False : return False



#   ____________________
#|--| Descontar Stock  |-----------------------------------------------------
def descontar_stock(lista_prods ,id ,cantidad):
    for producto in lista_prods:
        for clave, valor in producto.items():
            if clave == 'id' and valor == id:
                producto['stock'] = producto['stock'] - cantidad



#   ______________________
#|--| Filtrar Productos  |-----------------------------------------------------
def fitrador(filtro, buscar):
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
def buscador():
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
                    imprimir_producto(prod)
                else:
                    print('# *No se encontro el producto***')
            case "2":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el ID a Buscar')
                id_prod = int(input('|ID ···---: '))
                prod = fitrador('id', id_prod)
                if prod :
                    imprimir_producto(prod)
                else:
                    print('# *No se encontro el producto***')
            case "3":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Precio a Buscar')
                precio = float(input('|Precio ···---: $'))
                prod = fitrador('precio', precio)
                if prod :
                    imprimir_producto(prod)
                else:
                    print('# *No se encontro el producto***')
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')
        
        input('precione una tecla para continuar!')



#|--------  VENTAS  --------|#
#   __________________
#|--| Realizar Venta |-----------------------------------------------------
def realizar_venta():
    productos_auxiliar = []
    #productos_auxiliar = producto
    #productos_auxiliar = productos.copy()
    for producto in productos:
        productos_auxiliar.append(producto.copy())

    #limpiar_consola()
    descuento = False
    venta = {}
    list_prods = []
    total_venta = 0



    while True:
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        listar_productos(productos_auxiliar)
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        if len(list_prods) > 0:
            print('||||-Carrito:')
            for prod in list_prods:
                print(f'||-{mostrar_un_prod(prod['id_producto'])['nombre'].upper()} x {prod['detalle_prod']['cantidad']}')
            print(f'||\t\t\t·Total: ${total_venta:,}')
            print('|---------------------------------------------------------------------------')
        print('|-· Ingrese el Id del producto (Dejar vacio para continuar)')
        id_v = input('|##-· ID: ')

        if id_v == '':
            break        

        for producto in productos_auxiliar:
            if int(id_v) == producto['id']:
                cant = 0
                cant_str = ""
                cant_str = input('|##-· Cantidad: ')
                if cant_str == "":
                    cant = 1
                else:
                    cant = int(cant_str)
                if producto['stock'] > 0 and producto['stock'] >= cant:
                    v = {
                            'cantidad': cant,
                            'sub_total': (producto['precio'] * cant)  
                        }
                    total_venta = total_venta + (producto['precio'] * cant)
                    descontar_stock(productos_auxiliar,producto['id'],cant)
                    #producto['stock'] = producto['stock'] - cant
                    prod_venta = {
                        'id_producto': producto['id'],
                        'detalle_prod': v
                    }
                    if len(list_prods) > 0:
                        for prod_item in list_prods:
                            if prod_item['id_producto'] == prod_venta['id_producto']:
                                prod_item['detalle_prod']['cantidad'] +=  prod_venta['detalle_prod']['cantidad']
                            else:
                                list_prods.append(prod_venta)
                    else:
                        list_prods.append(prod_venta)
                else:
                    print('|# Producto Sin Stock')
                    input('precione una tecla para continuar!')
                    break
                print(f'|\t-{producto['nombre'].upper()} x {cant} Agregado a la compra') 
                input('precione una tecla para continuar!')



    venta["importe_total"] = total_venta


    if len(list_prods) > 0:
        venta['id_venta'] = len(ventas) + 1
        venta['detalle_venta'] = list_prods

        while True:
            limpiar_consola()
            print('|###--··  TecStore  ··--###|')

            for prod in list_prods:
                nom_prod = mostrar_un_prod(prod['id_producto'])['nombre'].upper()
                cant_prod = prod['detalle_prod']['cantidad']
                sub_total_prod = prod['detalle_prod']['sub_total']

                print(f'|-{nom_prod}{" " * (30 - len(nom_prod))} x {cant_prod} - ${sub_total_prod:,}')
            
            print(f'|\n|{"-" * 31}Total: ${total_venta:,}')

            print('|##-· Forma de pago')
            print('|· (1) Efectivo · (2) Transferencia · (3) Tarjeta · (0) Cancelar')
            op =  input('|##-Forma de Pago: ')
            match op:
                case '1':
                    venta['forma_pago'] = metodos_pago[int(op)-1]
                    break
                case '2':
                    venta['forma_pago'] = metodos_pago[int(op)-1]
                    break
                case '3':
                    venta['forma_pago'] = metodos_pago[int(op)-1]
                    break
                case "0":
                    print('|##- Venta Cancelada! ')
                    return
                case "":
                    print('|##- Venta Cancelada! ')
                    return
                case _:
                    print('Ingrese una opcion valida!')

        while True:
            print('|##-· Aplicar descuentos')
            print('|· (1) % Porcentaje · (2) $ Importe · (0) Sin Descuentos')
            opc = input('|##-Opcion: ')
            

            if opc == "1":
                desc = float(input('|#  ·Descuento: % '))
                venta['importe_total'] = float(venta['importe_total'])-(float(venta['importe_total'])*(desc/100))
                print(f'|-----------Importe Total ${total_venta:,} ')
                print(f'|-----------Importe con Descuento ${venta['importe_total']:,} ')
                descuento = True
                break
            elif opc == "2":
                desc = float(input('|#  ·Descuento: $ '))
                venta['importe_total'] = venta['importe_total'] - desc
                print(f'|-----------| Importe Total ${total_venta:,} ')
                print(f'|-----------| Importe con Descuento ${venta['importe_total']:,} ')
                descuento = True
                break
            elif opc == "0":
                print(f'|-----------Importe Actual ${venta['importe_total']:,}')
                break
            elif opc == "":
                print(f'|-----------Importe Actual ${venta['importe_total']:,}')
                break
            else:
                print(f'|# No se indico una opcion valida!')

        
        for prod_v in list_prods:
            descontar_stock(productos,prod_v['id_producto'],prod_v['detalle_prod']['cantidad'])
        ventas.append(venta)
        escribir_venta(venta)
        reescribir_productos_archivo()
        print("|##·· Se realizo la venta exitosamente! ··##|")
        input('precione una tecla para continuar!')
        limpiar_consola()

        print('|# Resumen de la venta!')
        print('|-- Productos')
        for prod in list_prods:
            prod_dicc = mostrar_un_prod(prod['id_producto'])
            prcio_prod = f'{prod_dicc['precio']:,}'
            linea = "| ·"
            
            linea += prod_dicc['nombre'].upper()
            linea += " " * (30 - len(prod_dicc['nombre'].upper()))
            linea += f'${prcio_prod} C/U '
            linea += " " * (11 - len(prcio_prod))
            linea += f'x {prod['detalle_prod']['cantidad']}'
            linea += f' - ${prod['detalle_prod']['sub_total']:,}'
            
            print(linea)
            
            #print(f'|-{nom_prod}{" " * (30 - len(nom_prod))} ${prod_dicc['precio']} C/U x {cant_prod}{" " *(11 - len(str(cant_prod)))} - ${sub_total_prod}')
        
        print(f'|-- Total: ${total_venta:,}')
        if descuento : print(f'|-- Total Neto(Descuento): ${venta['importe_total']:,}')
        print(f'|-- Forma de pago: {venta['forma_pago']}')

    input('precione una tecla para continuar!')



#   _________________
#|--| Listar Ventas |-----------------------------------------------------
def listar_ventas():
    print('|# Lista de Ventas')
    if len(ventas) == 0:
        print('|  ·No se emcontraron ventas!')
        input('precione una tecla para continuar!')
        return
    for venta in ventas:
        print(f'o- Venta Nroº: {venta['id_venta']}')
        print(' - Productos:')
        for prod_vent in venta['detalle_venta']:
            for producto in productos:
                if producto['id'] == prod_vent['id_producto']:
                    precio_prod = f'{producto['precio']:,}'
                    print(f'     ·{producto['nombre']}{(" " * ( 30 - len(producto['nombre']) ) )}- ${precio_prod}{(" " * ( 11 - len(precio_prod) ) )} - x {prod_vent['detalle_prod']['cantidad']} - SubTotal ${prod_vent['detalle_prod']['sub_total']:,} ')
        print(f' - Total: ${venta['importe_total']:,}')
        print(f' - Forma de pago: {venta['forma_pago']}')
        print('-········································')
    input('precione una tecla para continuar!')







# def ordenador_stock(orden):
#     if orden == 1:
        
#         return prod_stock
#     elif orden == 2:
        
#         return prod_stock


#--                                               --#
#----                                           ----#
#------                                       ------#
#--------     Funciones de Estadisticas     --------#
#------                                       ------#
#----                                           ----#
#--                                               --#


#|--------  PRODUCTOS --------|#
#   _____________________________
#|--| Estadisticas de Productos |-----------------------------------------------------
def estadisticas_productos():
    info_productos = {}

    cant_precio_total = 0
    cant_total = 0
    for producto in productos:
        cant_total = cant_total + int(producto['stock'])
        cant_precio_total = cant_precio_total + (float(producto['precio'])*int(producto['stock']))
    
    prod_mas_stock = sorted(productos, key=lambda prod: prod['stock'],reverse=True)
    prod_menos_stock = sorted(productos, key=lambda prod: prod['stock'])
    
    info_productos.update({'capital_neto':cant_precio_total})
    info_productos.update({'cantidad_existencias':cant_total})
    info_productos.update({'prod_stock_bajo':prod_mas_stock[0]})
    info_productos.update({'prod_stock_alto':prod_menos_stock[0]})

    return info_productos




#|--------  VENTAS --------|#
#   __________________________
#|--| Estadisticas de Ventas |-----------------------------------------------------
def estadisticas_ventas():
    info_ventas = {}

    cant_ventas = len(ventas)
    cant_ganancias = 0

    ganancias_totales = 0
    #ganancias_netas = 0

    metodos_contados = {
        # 'efectivo':{
        #  'veces_usado' : 4
        #  'importe_metodo' : 70000
        # }
    }

    prod_vendidos = {
        # 3 : {
        #     # 'nombre' : 'prueba',
        #     # 'cantidad_vendidos': 5
        # }
    }
    

    # {
#         "id_venta": 2,
#         "detalle_venta": [{
#             'id_producto': 1,
#             'detalle_prod':
#             {
#                    'cantidad': 1,
#                    'sub_total': 50  
#             }              
#            }],
#         "importe_total": 50000,
#         "forma_pago": 'Tarjeta'
#     },

    for venta in ventas:
        cant_ganancias = cant_ganancias + float(venta['importe_total'])
        for prod_det_vent in venta['detalle_venta']:
            p = {}
            nombre = ""
            cant_prod_v = 0
        
        ganancias_totales = + ganancias_totales

        for clave, valor in prod_vendidos.items():
            if clave == 'id_prod' and prod_det_vent['id_producto'] == valor:
                cant_prod_v = int(prod_vendidos['cantidad_vendidos']) + int(prod_det_vent['detalle_prod']['cantidad'])

        if cant_prod_v == 0:
            cant_prod_v = int(prod_det_vent['detalle_prod']['cantidad'])
        nombre = mostrar_un_prod(prod_det_vent['id_producto'])['nombre']

        p = {
            prod_det_vent['id_producto']:{
                'nombre': nombre,
                'cantidad_vendidos': cant_prod_v
            }
        }
        prod_vendidos.update(p)

          
        forma_p = ""
        metodo = {}
        cont_metodo = 0
        importe_metodo = 0
        if venta['forma_pago'] in metodos_contados:
            forma_p = venta['forma_pago']
            for clave, valor in metodos_contados[forma_p].items():
                if clave == 'veces_usado':
                    cont_metodo = valor + 1
                elif clave == 'importe_metodo':
                    importe_metodo = valor + venta['importe_total']
        else:
            forma_p = venta['forma_pago']
            metodo = {}
            cont_metodo = 1
            importe_metodo = venta['importe_total']
        
        metodo.update({'veces_usado':cont_metodo})
        metodo.update({'importe_metodo':importe_metodo})

        metodos_contados.update({venta['forma_pago']:metodo})

    prod_menos_vendido = []
    prod_mas_vendido = []
    prod_menos_vendido = sorted(prod_vendidos.items(), key=lambda prod: prod[1]['cantidad_vendidos'])
    prod_mas_vendido = sorted(prod_vendidos.items(), key=lambda prod: prod[1]['cantidad_vendidos'], reverse=True)
    # print(prod_menos_vendido)
    # print(prod_mas_vendido)


    metodo_menos_usado = []
    metodo_mas_usado = []
    metodo_menos_usado = sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['veces_usado'])
    metodo_mas_usado = sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['veces_usado'], reverse=True)
    # print(metodo_menos_usado)
    # print(metodo_mas_usado)

    metodo_mas_recaudado= []
    metodo_menos_recaudado= []
    metodo_mas_recaudado= sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['importe_metodo'])
    metodo_menos_recaudado = sorted(metodos_contados.items(), key=lambda metodo: metodo[1]['importe_metodo'], reverse=True)
    # print(metodo_menos_recaudado)
    # print(metodo_mas_recaudado)


    # print('|-Cantidad de ventas: 99 - $999999')
    info_ventas.update({'cantidad_venta': cant_ventas})
    info_ventas.update({'cantidad_ganancia': cant_ganancias})


    # print('|-Producto Mas Vendido: teclado - ventas: 22')
    info_ventas.update({'prod_mas_vendidos':prod_mas_vendido[0]})
    # print('|-Producto Menos Vendido: teclado - ventas: 2')
    info_ventas.update({'prod_menos_vendidos':prod_menos_vendido[0]})

    # print('|-Metodo de Pago mas usado: efectivo - $99999')
    info_ventas.update({'metodo_mas_usado':metodo_mas_usado[0]})
    # print('|-Metodo de Pago menos usado: tarjeta - $1000')
    info_ventas.update({'metodo_menos_usado':metodo_menos_usado[0]})


    # print('|-Metodo de Pago que mas recaudo: efectivo - $99999')
    info_ventas.update({'metodo_menos_recaudado':metodo_mas_recaudado[0]})
    # print('|-Metodo de Pago que menos recaudo: tarjeta - $1000')
    info_ventas.update({'metodo_mas_recaudado':metodo_menos_recaudado[0]})

    return info_ventas




#|--------  GENERAL --------|#
#   __________________________
#|--| Estadisticas Generales |-----------------------------------------------------
def estadisticas_generales():
    limpiar_consola()
    print('|###--··  TecStore  ··--###|')
    stats_prod=estadisticas_productos()
    stats_vent=estadisticas_ventas()
    print('|##·· Estadisticas Generales')
    print(f'|-Cantidad de productos registrados: {len(productos)}')
    print(f'|-Cantidad de Ventas Totales: {stats_vent['cantidad_venta']} - Recaudado: ${stats_vent['cantidad_ganancia']:,}')
    print('|')
    print('|##·· Estadisticas Productos')
    print(f'|-Producto Mas Vendido: {stats_vent['prod_mas_vendidos'][1]['nombre']} - vendidos: {stats_vent["prod_mas_vendidos"][1]['cantidad_vendidos']}')
    print(f'|-Producto Menos Vendido: {stats_vent['prod_menos_vendidos'][1]['nombre']} - vendidos: {stats_vent["prod_menos_vendidos"][1]['cantidad_vendidos']}')
    print('|')
    print('|##·· Estadisticas Stock')
    print(f'|-Cantidad total de Productos: {stats_prod['cantidad_existencias']} - capital: ${stats_prod['capital_neto']:,}')
    print(f'|-Producto con mas Stock: {stats_prod['prod_stock_bajo']['nombre']} - stock: {stats_prod['prod_stock_bajo']['stock']}')
    print(f'|-Producto con menos Stock: {stats_prod['prod_stock_alto']['nombre']} - stock: {stats_prod['prod_stock_alto']['stock']}')
    print('|')
    print('|##·· Estadisticas Metodos de Pago')
    print(f'|-Mas usado: {stats_vent['metodo_mas_usado'][0]} ({stats_vent['metodo_mas_usado'][1]['veces_usado']} veces) - ${stats_vent['metodo_mas_usado'][1]['importe_metodo']:,}')
    print(f'|-Menos usado: {stats_vent['metodo_menos_usado'][0]} ({stats_vent['metodo_menos_usado'][1]['veces_usado']} veces) - ${stats_vent['metodo_menos_usado'][1]['importe_metodo']:,}')
    print(f'|-Metodo que mas recaudo: {stats_vent['metodo_mas_recaudado'][0]} - ${stats_vent['metodo_mas_recaudado'][1]['importe_metodo']:,}')
    print(f'|-Metodo que menos recaudo: {stats_vent['metodo_menos_recaudado'][0]} - ${stats_vent['metodo_menos_recaudado'][1]['importe_metodo']:,}')
    print('|##················································')
    input('precione una tecla para continuar!')




#------                                ------#
#--------     Funciones auxiliar     --------#
#------                                ------#

#   _______________________________________
#|--| Sincronizacion de datos con Archivo |-----------------------------------------------------
def sincronisar_datos():
    extraer_productos()
    extraer_ventas()




#--                                      --#
#----                                  ----#
#------                              ------#
#--------      Menu De Inicio      --------#
#------                              ------#
#----                                  ----#
#--                                      --#



#|--------  Inicio del Programa   --------|#
#   _________________
#|--| Menu de Inicio|-----------------------------------------------------

if __name__ == "__main__":
    
    sincronisar_datos()
    while True:
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        print('|##······················##|')
        print('| 1 ) --- Gestion de Producto') 
        print('| 2 ) --- Mostrar Productos')
        print('| 3 ) --- Modificar Stock') 
        print('| 4 ) --- Realizar Venta')
        print('| 5 ) --- Mostrar Ventas')
        print('| 6 ) --- Buscar Producto')
        print('| 7 ) --- Eliminar Producto')
        print('| 8 ) --- Estadisticas de Ventas')
        print('| 0 ) --- Salir')
        op = input('|OPCION···---: ')

        limpiar_consola()
        match op:
            case "1":
                abm_producto()
            case "2":
                print('|·# Productos')
                listar_productos(productos)
                input('precione una tecla para continuar!')
            case "3":
                mod_stock_prod()
            case "4":
                realizar_venta()
            case "5":
                listar_ventas()
            case "6":
                buscador()
            case "7":
                eliminar_producto()
            case "8":
                estadisticas_generales()
            case "0":
                print('Saliendo.....')
                break
            case _:
                print('Ingrese una opcion valida!')
            
        #input('precione una tecla para continuar!')

