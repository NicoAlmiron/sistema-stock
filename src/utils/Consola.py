from src.exceptions.excepciones import DatoNumericoObligatorio, DniRegistrado, AuthenticationError, OpcionInvalida, TecStoreError
from src.persistensia import extraer_productos
from src.classes.Usuario import Usuario
from src.services.Producto_services import agregar_prod, listar_productos, mod_stock_prod, mod_prod, eliminar_producto
from src.services.Ventas_services import realizar_venta, listar_ventas
from src.services.Usuario_services import definir_id, registrar_usuario, autenticar_usuario, verificar_permisos, pedir_dni, listar_usuarios,lista_usuarios_activos,lista_usuarios_suspendidos
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
            try:
                op = input('|OPCION···---: ')
                limpiar_consola()
                match op:
                    case "1":
                        abm_producto()
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
                    case "9":
                        abm_usuarios()
                    case "0":
                        cerrar_sesion(vendedor)
                        print('Saliendo.....')
                        break
                    case _:
                        raise OpcionInvalida()
                    
            except TecStoreError as e:
                print(e)
                input( '|##······················##|')
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
        try:
            user = autenticar_usuario(dni, clave)
            print(f'|# BIENVENIDO {user.nombre}')
            input( '|##······················##|')
            return crear_sesion(user)
        except AuthenticationError as e:
            print(e)
            input( '|##······················##|')


#   ___________________________________
#|--| Sub-Menu de registro de usuario |-----------------------------------------------------
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
                raise TecStoreError()
            
        except TecStoreError as e:
            input(e)
            break



#   _________________________________
#|--| Sub-Menu de gestion Productos |-----------------------------------------------------
def abm_producto():
    while True:
        limpiar_consola()
        cabecera_menu()
        print('| 1 ) --- Agregar Nuevo')
        print('| 2 ) --- Modificar Existente')
        print('| 3 ) --- Modificar Stock')
        print('| 4 ) --- Eliminar')
        print('| 5 ) --- Listar Productos')
        print('| 0 ) --- Volver')

        try:

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
                case "5":
                    listar_productos()
                case "0":
                    break
                case _:
                    raise OpcionInvalida()

            input('precione una tecla para continuar!')

        except TecStoreError as e:
            print(e)

#   ________________________________
#|--| Sub-Menu de gestion Usuarios |-----------------------------------------------------
def abm_usuarios():
    while True:
        limpiar_consola()
        cabecera_menu()
        print('| 1 ) --- Registrar Usuario')
        print('| 2 ) --- Usuarios Activos')
        print('| 3 ) --- Usuarios Suspendidos')
        print('| 4 ) --- Usuarios General')
        #print('| 5 ) --- Suspender Usuario')
        print('| 0 ) --- Volver')

        try:
            op = input('|OPCION···---: ')

            limpiar_consola()
            match op:
                case "1":
                    menu_registrar_usuario()
                case "2":
                    cabecera_menu()
                    listar_usuarios(lista_usuarios_activos())
                case "3":
                    cabecera_menu()
                    listar_usuarios(lista_usuarios_suspendidos())
                case "4":
                    cabecera_menu()
                    listar_usuarios()
                #case "5":
                case "0":
                    break
                case _:
                    raise OpcionInvalida()

            input('precione una tecla para continuar!')

        except TecStoreError as e:
            input(e)