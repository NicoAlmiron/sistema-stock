from src.exceptions.excepciones import OpcionInvalida, TecStoreError
from src.model.Sesion import Sesion
from src.persistensia.Gestion_Producto import Gestion_Producto
from src.persistensia.Gestion_Usuario import Gestion_Usuario
from src.services.Producto_services import agregar_prod, mod_stock_prod, mod_prod, eliminar_producto, reactivacion_producto, buscador
from src.services.Ventas_services import realizar_venta, listar_ventas
from src.services.Usuario_services import registrar_usuario, suspender_usuario, reactivar_usuario
from src.persistensia.Gestion_Sesion import Gestion_Sesion
from .Helpers import limpiar_consola, cabecera_menu


# Menu Principal

def menuPrincipal(vendedor):
    productos = Gestion_Producto().extraer_productos()
    while True:
            limpiar_consola()
            cabecera_menu()
            print('| 1 ) --- Mostrar Productos')
            print('| 2 ) --- Realizar Venta')
            print('| 3 ) --- Mostrar Ventas')
            print('| 4 ) --- Buscar Producto')
            print('| 5 ) --- Estadisticas de Ventas')
            if vendedor.verificar_permisos():
                print('| 6 ) --- Gestion de Producto') 
                print('| 7 ) --- Modificar Stock') 
                print('| 8 ) --- Gestion de Usuario') # solo admin
            print('| 0 ) --- Salir')
            try:
                op = input('|OPCION···---: ')
                limpiar_consola()
                match op:
                    case "1":
                        cabecera_menu()
                        print('|·# Productos')
                        Gestion_Producto().listar_productos(productos)
                        input('precione una tecla para continuar!')
                    case "2":
                        realizar_venta(vendedor)
                    case "3":
                        listar_ventas()
                    case "4":
                        buscador()
                #    case "5":
                #        estadisticas_generales()
                    case "6":
                        if vendedor.verificar_permisos():
                            abm_producto(vendedor)
                        else:
                            raise OpcionInvalida()
                    case "7":
                        if vendedor.verificar_permisos():
                            mod_stock_prod()
                        else:
                            raise OpcionInvalida()
                    case "8":
                        if vendedor.verificar_permisos():
                            abm_usuarios()
                        else:
                            raise OpcionInvalida()
                    case "0":
                        Gestion_Sesion().guardar_sesion(vendedor)
                        print('Saliendo.....')
                        break
                    case _:
                        raise OpcionInvalida()
                    
            except TecStoreError as e:
                print(e)
                input( '|##······················##|')
            #input('precione una tecla para continuar!')
    




#   _________________________________
#|--| Sub-Menu de gestion Productos |-----------------------------------------------------
def abm_producto(vendedor):
    while True:
        limpiar_consola()
        cabecera_menu()
        print('| 1 ) --- Agregar Nuevo')
        print('| 2 ) --- Modificar Existente')
        print('| 3 ) --- Modificar Stock')
        print('| 4 ) --- Eliminar')
        print('| 5 ) --- Listar Productos')
        print('| 6 ) --- Reactivar')
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
                    cabecera_menu()
                    print('|·# Productos')
                    Gestion_Producto().listar_productos()
                    input('precione una tecla para continuar!')
                case "6":
                    reactivacion_producto()
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
        print('| 5 ) --- Suspender Usuario')
        print('| 6 ) --- Reactivar Usuario')
        print('| 0 ) --- Volver')

        try:
            op = input('|OPCION···---: ')

            limpiar_consola()
            match op:
                case "1":
                    registrar_usuario()
                case "2":
                    Gestion_Usuario().lista_usuarios_activos()
                case "3":
                    Gestion_Usuario().lista_usuarios_suspendidos()
                case "4":
                    cabecera_menu()
                    Gestion_Usuario().listar_usuarios()
                case "5":
                    suspender_usuario()
                case "6":
                    reactivar_usuario()
                case "0":
                    break
                case _:
                    raise OpcionInvalida()

            input('precione una tecla para continuar!')

        except TecStoreError as e:
            input(e)