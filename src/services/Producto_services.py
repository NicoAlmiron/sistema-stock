from src.persistensia import escribir_productos, extraer_productos
from src.utils.Helpers import limpiar_consola
from src.classes import Producto



#------                                           ------#
#--------               PRODUCTOS               --------#
#------                                           ------#


#|--------  PRODUCTOS --------|#
#   ____________________
#|--| Agregar Producto |-----------------------------------------------------
def agregar_prod():

    productos = extraer_productos()

    producto = Producto(None, None, None, None)
    print('|###--··  TecStore  ··--###|')
    print('|##-· Producto Nuevo')

    ultima_pocicion =  len(productos)-1
    Producto.id_producto = productos[ultima_pocicion].id + 1
    print(f'|##-· Producto ID: {Producto.id_producto}')

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
        producto.nombre = nombre_prod

    

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
        producto.precio = float(precio_prod)


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
        producto.stock = int(stock_prod)


    productos.append(producto)
    escribir_productos(productos)
    print("Se Guardo el producto exitosamente!")


#   ______________________
#|--| Modificar Producto |-----------------------------------------------------
def mod_prod(productos):
    producto = Producto(None, None, None, None)
    print('|###--··  TecStore  ··--###|')
    listar_productos(productos)
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for i , prod in enumerate(productos):
        if prod.id == int(id_buscar):
            print(f'|##-· Producto ID: {prod.id}')
            
            print(f"|-Nobre anterior *{prod.nombre}*")
            nombre_nuevo = input('|-Nobre del articulo: ')
            if len(nombre_nuevo) > 30:
                print("# **Se exedio el limite de caracteres**")  
                input('precione una tecla para continuar!') 
                return        
            elif nombre_nuevo != "":
                productos[i].nombre = nombre_nuevo
            print(f"|-Precio anterior $*{prod.precio:,}*".replace(",","."))
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
                    productos[i].precio = float(precio_nuevo)
            #prod.update(producto)  
            break

    escribir_productos(productos)
    print("Se Guardo el producto exitosamente!")


#   _______________________________
#|--| Modificar Stock de Producto |-----------------------------------------------------
def mod_stock_prod():
    productos = extraer_productos()
    print('|###--··  TecStore  ··--###|')
    listar_productos(productos)
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for i, prod in enumerate(productos):
        if prod.id == int(id_buscar):   
            print(f"| {prod.nombre}*")
            print(f"| -Stock actual *{prod.stock}*")
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
                productos[i].stock = int(stock_nuevo)
    escribir_productos(productos)
    print("Se actualizo el stock exitosamente!")

#   _____________________
#|--| Eliminar Producto |-----------------------------------------------------
def eliminar_producto(productos):
    print('|###--··  TecStore  ··--###|')
    print('|##-· Ingrese el Id del producto')
    id_buscar = input('|##-· ID: ')
    for i, prod in enumerate(productos):
        if prod.id == int(id_buscar):
            print(f"\n# Producto: {prod.nombre.upper()} - ${prod.precio:,}\n")
            print(f"# *Esta seguro que quiere eliminar este Producto?")
            print( '#     Confirmar - 1   |    Cancelar - 0')
            opcion = input("#Opcion: ")       
            if opcion != "":
                if opcion == "0":
                    print("#   **Se Cancelo la operacion!**")                    
                elif opcion == "1":
                    productos.remove(prod)
                    print("Se Elimino el Producto exitosamente!")
                    escribir_productos(productos)
                else:
                    print("#   **Se Cancelo la operacion!**")
            else:
                print("#   **Se Cancelo la operacion!**")





#   ____________________
#|--| Listar Productos |-----------------------------------------------------
def listar_productos(lista_productos):

    if lista_productos:
        for i, producto in enumerate(lista_productos):
            print(producto)
    else:
        print('|\t·No se emcontraron productos!')
        

# def imprimir_producto(producto):
#    precio_prod = f'{producto.precio:,}'
#    renglon = f'|ID: {Producto.id_producto}{(" " * ( 6 - len(str(Producto.id_producto)) ) )}'
#    renglon += f'| {producto.nombre}{(" " * ( 30 - len(producto.nombre) ) )}'
#    renglon += f'| ${producto.precio:,}{(" " * ( 13 - len(precio_prod)))}'
#    renglon += f'| STOCK: {producto.stock}'
#    if int(producto.stock) < 4 and int(producto.stock) > 0:
#        renglon += ' (STOCK BAJO)'
#    elif int(producto.stock) == 0:
#        renglon += ' (SIN STOCK!!*!*!*!)'
#    print(renglon)

#   ________________________________
#|--| Mostrar un producto por 'id' |-----------------------------------------------------
def mostrar_un_prod(id, productos):
    encontrado = False
    for producto in productos:
        if Producto.id_producto == id:
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
                    #imprimir_producto(prod)
                else:
                    print('# *No se encontro el producto***')
            case "2":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el ID a Buscar')
                id_prod = int(input('|ID ···---: '))
                prod = fitrador('id', id_prod)
                if prod :
                    print(prod)
                    #imprimir_producto(prod)
                else:
                    print('# *No se encontro el producto***')
            case "3":
                print('|###--··  TecStore  ··--###|')
                print('|##--- Ingrese el Precio a Buscar')
                precio = float(input('|Precio ···---: $'))
                prod = fitrador('precio', precio)
                if prod :
                    print(prod)
                    #imprimir_producto(prod)
                else:
                    print('# *No se encontro el producto***')
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')
        
        input('precione una tecla para continuar!')


