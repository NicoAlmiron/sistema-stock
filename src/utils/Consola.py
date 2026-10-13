from src.exceptions.excepciones import DatoNumericoObligatorio, DniRegistrado
from src.persistensia import extraer_productos
from src.classes.Usuario import Usuario
from src.services.Producto_services import agregar_prod, listar_productos, mod_stock_prod, mod_prod, eliminar_producto
from src.services.Ventas_services import realizar_venta, listar_ventas
from src.services.Usuario_services import definir_id, registrar_usuario, autenticar_usuario, verificar_permisos, pedir_dni
from src.services.Actividad_services import crear_sesion,cerrar_sesion
from .Helpers import limpiar_consola, hashear_clave, pedir_telefono, definir_rol, definir_clave, cabecera_menu


# Menu Principal

def menuPrincipal(vendedor):
    productos = extraer_productos()
    while True:
            limpiar_consola()
            cabecera_menu()
            print('| 1 ) --- Gestion de Producto') 
            print('| 2 ) --- Mostrar Productos')
            print('| 3 ) --- Modificar Stock') 
            print('| 4 ) --- Realizar Venta')
            print('| 5 ) --- Mostrar Ventas')
            #print('| 6 ) --- Buscar Producto')
            #print('| 7 ) --- Eliminar Producto')
            #print('| 8 ) --- Estadisticas de Ventas')
            if verificar_permisos(vendedor):
                print('| 9 ) --- Gestion de Usuario') # solo admin
            print('| 0 ) --- Salir')
            op = input('|OPCION···---: ')
    
            limpiar_consola()
            match op:
                case "1":
                    abm_producto(vendedor)
                case "2":
                    cabecera_menu()
                    print('|·# Productos')
                    listar_productos(productos)
                    input('precione una tecla para continuar!')
                case "3":
                    mod_stock_prod()
                case "4":
                    realizar_venta(vendedor)
                case "5":
                    listar_ventas()
            #    case "6":
            #        buscador()
            #    case "7":
            #        eliminar_producto()
            #    case "8":
            #        estadisticas_generales()
            #    case "9":

                case "0":
                    cerrar_sesion(vendedor)
                    print('Saliendo.....')
                    break
                case _:
                    print('Ingrese una opcion valida!')
                
            #input('precione una tecla para continuar!')
    

# Login

def Login():
    while True:
        limpiar_consola()
        cabecera_menu()
        print('|##···INICIO DE SESION···##|')
        dni = input('|#-DNI: ')
        clave = input('|#-CONTRASEÑA: ')
        limpiar_consola()
        cabecera_menu()
        if autenticar_usuario(dni, clave):
            user = autenticar_usuario(dni, clave)
            print(f'|# BIENVENIDO {user.nombre}')
            input( '|##······················##|')
            return crear_sesion(user)
        else:
            print(f'|·· *ERROR* - USUARIO Y/O  |')
            print( '| CONTRASEÑA INCORRECTOS ··|')
            input( '|##······················##|')



def menu_registrar_usuario():
    while True:
        try:
            limpiar_consola()
            cabecera_menu()
            print('|##··REGISTROS DE DATOS··##|')
            id_usuario = definir_id()
            nombre = input('|#-NOMBRE: ')
            dni = pedir_dni()            
            telefono = pedir_telefono()
            rol = definir_rol()
            clave = definir_clave()

            sal = None
            hash = None
            sal, hash = hashear_clave(clave)

            usuario = Usuario(id_usuario, nombre, dni, telefono, rol, sal, hash)

            if registrar_usuario(usuario):
                print("|· Usuario registrado con exito!")
                return
            else:
                input("|· Sucedio un error al crear el usuario")

        except DatoNumericoObligatorio as e:
            input(f"Error: {e}")
        except ValueError:
            input(f"Ingrese un numero!")
        except DniRegistrado as er:
            input(f"Error: {er}")



#   _________________________________
#|--| Sub-Menu de gestion Productos |-----------------------------------------------------
def abm_producto(usuario):
    productos = []

    while True:
        limpiar_consola()
        cabecera_menu()
        print('| 1 ) --- Agregar Nuevo')
        print('| 2 ) --- Modificar Existente')
        print('| 3 ) --- Modificar Stock')
        print('| 4 ) --- Eliminar')
        print('| 5 ) --- Listar Productos')
        print('| 0 ) --- Salir')
        op = input('|OPCION···---: ')

        limpiar_consola()
        match op:
            case "1":
                agregar_prod()
            case "2":
                mod_prod(productos)
            case "3":
                mod_stock_prod(productos)
            case "4":
                eliminar_producto(productos)
            case "5":
                productos = extraer_productos()
                listar_productos(extraer_productos())
            case "0":
                break
            case _:
                print('Ingrese una opcion valida!')

        input('precione una tecla para continuar!')
