from src.exceptions.excepciones import OpcionInvalida, TecStoreError
from src.services.Producto_services import (agregar_prod, mod_stock_prod, mod_prod, eliminar_producto,
                                            reactivacion_producto, buscador, listar_productos)
from src.services.Ventas_services import realizar_venta, listar_ventas, exportar_historial_csv
from src.services.Usuario_services import (registrar_usuario, suspender_usuario, reactivar_usuario,
                                           listar_usuarios, listar_usuarios_activos, listar_usuarios_suspendidos)
from src.persistensia.Gestion_Sesion import Gestion_Sesion
from .Helpers import limpiar_consola, cabecera_menu, guion_titulo, guion_base, guion_item, guion_opcion, pedir_opcion
from .Helpers import pausar_consola
from src.services.Estadisticas_services import menu_estadisticas



def menuPrincipal(vendedor):
    while True:
            limpiar_consola()
            cabecera_menu()
            guion_titulo('MENU PRINCIPAL')
            guion_titulo('')
            guion_opcion("1","Mostrar Productos")
            guion_opcion("2","Realizar Venta")
            guion_opcion("3","Mostrar Ventas")
            guion_opcion("4","Buscar Producto")
            guion_opcion("5","Estadisticas")
            if vendedor.verificar_permisos():
                guion_opcion("6","Gestion de Producto")
                guion_opcion("7","Modificar Stock")
                guion_opcion("8","Gestion de Usuario")
                guion_opcion("9","Exportar CSV Historial Ventas")
            guion_opcion("0","Salir")
            guion_titulo('')
            try:

                op = pedir_opcion(input(f'|{" "*31}OPCION···---: '))
                limpiar_consola()

                match op:
                    case "1":
                        mostrar_lista_prods()
                    case "2":
                        realizar_venta(vendedor)
                    case "3":
                        listar_ventas()
                    case "4":
                        buscador()
                    case "5":
                        menu_estadisticas(vendedor)
                    case "6":
                        if vendedor.verificar_permisos():
                            abm_producto()
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
                    case "9":
                        if vendedor.verificar_permisos():
                            exportar_historial_csv()
                        else:
                            raise OpcionInvalida()
                    case "0":
                        pausar_consola('Saliendo.....')
                        break
                    case _:
                        raise OpcionInvalida()
                    
            except TecStoreError as e:
                cabecera_menu()
                pausar_consola(e.mensaje)
    




#   _________________________________
#|--| Sub-Menu de gestion Productos |-----------------------------------------------------
def abm_producto():
    while True:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('ADMINISTRACION DE PRODUCTOS')
        guion_titulo('')
        guion_opcion("1","Agregar Nuevo")
        guion_opcion("2","Listar Productos")
        guion_opcion("3","Modificar Existente")
        guion_opcion("4","Modificar Stock")
        guion_opcion("5","Eliminar")
        guion_opcion("6","Reactivar")
        guion_opcion("0","Volver")

        try:

            op = pedir_opcion(input(f'|{" "*31}OPCION···---: '))

            limpiar_consola()
            match op:
                case "1":
                    agregar_prod()
                case "2":
                    mostrar_lista_prods()
                case "3":
                    mod_prod()
                case "4":
                    mod_stock_prod()
                case "5":
                    eliminar_producto()
                case "6":
                    reactivacion_producto()
                case "0":
                    break
                case _:
                    raise OpcionInvalida()

        except TecStoreError as e:
            pausar_consola(e.mensaje)

#   ________________________________
#|--| Sub-Menu de gestion Usuarios |-----------------------------------------------------
def abm_usuarios():
    while True:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('ADMINISTRACION DE PRODUCTOS')
        guion_titulo('')
        guion_opcion("1","Registrar Usuario")
        guion_opcion("2","Usuarios Activos")
        guion_opcion("3","Usuarios Suspendidos")
        guion_opcion("4","Usuarios General")
        guion_opcion("5","Suspender Usuario")
        guion_opcion("6","Reactivar Usuario")
        guion_opcion("0","Volver")

        try:
            op = input(f'|{" "*31}OPCION···---: ')

            limpiar_consola()
            match op:
                case "1":
                    registrar_usuario()
                case "2":
                    listar_usuarios_activos()
                case "3":
                    listar_usuarios_suspendidos()
                case "4":
                    cabecera_menu()
                    listar_usuarios()
                case "5":
                    suspender_usuario()
                case "6":
                    reactivar_usuario()
                case "0":
                    break
                case _:
                    raise OpcionInvalida()

            pausar_consola()

        except TecStoreError as e:
            pausar_consola(e.mensaje)


def mostrar_lista_prods():
    cabecera_menu()
    guion_titulo('Listado de Productos')
    guion_base("")
    listar_productos()
    guion_base("")
    guion_titulo('')
    pausar_consola()