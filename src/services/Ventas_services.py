from src.utils.Helpers import limpiar_consola, cabecera_menu, pedir_id, pedir_stock, pedir_precio
from .Producto_services import  descontar_stock
from src.persistensia.Gestion_Producto import Gestion_Producto
from src.persistensia.Gestion_Venta import Gestion_Venta
from src.exceptions.excepciones import TecStoreError, VentaCancelada, OperacionCancelada

from src.model import Venta, DetalleVenta


metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")

#|--------  VENTAS  --------|#
#   __________________
#|--| Realizar Venta |-----------------------------------------------------
def realizar_venta(vendedor):

    productos = Gestion_Producto().extraer_productos()

    #descuento = False

    venta = Venta(id_venta=None, forma_pago=None,importe_total= None,detalle_venta=None,vendedor_nombre=vendedor.nombre,id_vendedor= vendedor.id_usuario)

    list_prods = []

    total_venta = 0
    try:
        while True:
            try:
                limpiar_consola()
                cabecera_menu()
                Gestion_Producto().listar_productos(productos)
                print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                if len(list_prods) > 0:
                    print('||||-Carrito:')
                    for prod in list_prods:
                        print(prod)
                    print(f'||\t\t\t·Total: ${total_venta:,}')
                    print('|---------------------------------------------------------------------------')
                print('|-· Ingrese el Id del producto (Dejar vacio para continuar)')
                id_prod_v = pedir_id(input('|##-· ID: '))  

                for i, producto in enumerate(productos):
                    if id_prod_v == producto.id_producto:
                        cant = 0
                        cant = pedir_stock(input('|##-· Cantidad: '))
                        if producto.verificar_stock(cant):

                            det_prod_ven = DetalleVenta(
                                id_producto=producto.id_producto,
                                nombre = producto.nombre,
                                precio=producto.precio,
                                stock=producto.stock,
                                id_venta=None,
                                cantidad=cant,
                                subtotal=producto.precio * cant
                            )

                            
                            total_venta = total_venta + (producto.precio * cant)

                            productos = descontar_stock(productos,producto.id_producto,cant)

                            nuevoProd = True

                            if len(list_prods) > 0:
                                for i, prod_item in enumerate(list_prods):
                                    if prod_item.id_producto == det_prod_ven.id_producto:
                                        list_prods[i].cantidad =  det_prod_ven.cantidad + prod_item.cantidad
                                        nuevoProd = False
                                if nuevoProd:
                                    list_prods.append(det_prod_ven)
                            else:
                                list_prods.append(det_prod_ven)
                        print(f'|\t-{producto.nombre.upper()} x {cant} Agregado a la compra') 
                        input('precione una tecla para continuar!')
            except OperacionCancelada:

                venta.importe_total = total_venta

                if list_prods is not []:
                    venta.id_venta = Gestion_Venta().definir_id()
                    venta.detalle_venta = list_prods

                    while True:
                        limpiar_consola()
                        print('|###--··  TecStore  ··--###|')

                        for prod in list_prods:
                            print(prod)

                            #print(f'|-{nom_prod}{" " * (30 - len(nom_prod))} x {cant_prod} - ${sub_total_prod:,}')
                        
                        print(f'|\n|{"-" * 31}Total: ${total_venta:,}')

                        print('|##-· Forma de pago')
                        print('|· (1) Efectivo · (2) Transferencia · (3) Tarjeta · (0) Cancelar')
                        op =  input('|##-Forma de Pago: ')
                        match op:
                            case '1':
                                venta.forma_pago = metodos_pago[int(op)-1]
                                break
                            case '2':
                                venta.forma_pago = metodos_pago[int(op)-1]
                                break
                            case '3':
                                venta.forma_pago = metodos_pago[int(op)-1]
                                break
                            case "0":
                                raise VentaCancelada()
                            case "":
                                raise VentaCancelada()
                            case _:
                                raise OperacionCancelada()

                    while True:
                        if vendedor.verificar_permisos() == "ADMINISTRADOR":

                            print('|##-· Aplicar descuentos')
                            print('|· (1) % Porcentaje · (2) $ Importe · (0) Sin Descuentos')
                            opc = input('|##-Opcion: ')
                            

                            if opc == "1":
                                venta.descuento_porcentaje(pedir_stock(input('|#  ·Descuento: $ ')))
                                
                                print(f'|-----------Importe Total ${total_venta:,} ')
                                print(f'|-----------Importe con Descuento ${venta.importe_total:,} ')
                                descuento = True
                                break
                            elif opc == "2":
                                venta.descuento_importe(pedir_precio(input('|#  ·Descuento: % ')))
                                print(f'|-----------| Importe Total ${total_venta:,} ')
                                print(f'|-----------| Importe con Descuento ${venta.importe_total:,} ')
                                descuento = True
                                break
                            elif opc == "0":
                                print(f'|-----------Importe Actual ${venta.importe_total:,}')
                                break
                            elif opc == "":
                                print(f'|-----------Importe Actual ${venta.importe_total:,}')
                                break
                            else:
                                print(f'|# No se indico una opcion valida!')
                        elif opc == "0":
                            print(f'|-----------Importe Actual ${venta.importe_total:,}')
                            break
                    gestion_venta = Gestion_Venta(venta=venta, productos=list_prods)

                    gestion_venta.procesar_venta()
                    Gestion_Producto().escribir_productos(productos)
                    print("|##·· Se realizo la venta exitosamente! ··##|")
                    input('precione una tecla para continuar!')
                    limpiar_consola()

                    print('|# Resumen de la venta!')
                    print('|-- Productos')

                    for i,prod in enumerate(list_prods):
                        prod_dicc = list_prods[i]
                        prcio_prod = f'{prod_dicc.precio:,}'
                        linea = "| ·"
                        
                        linea += prod_dicc.nombre.upper()
                        linea += " " * (30 - len(prod_dicc.nombre.upper()))
                        linea += f'${prcio_prod} C/U '
                        linea += " " * (11 - len(prcio_prod))
                        linea += f'x {prod_dicc.cantidad}'
                        linea += f' - ${prod_dicc.subtotal:,}'
                        
                        print(linea)
                    
                    print(f'|-- Total: ${total_venta:,}')
                    if descuento : print(f'|-- Total Neto(Descuento): ${venta.importe_total:,}')
                    print(f'|-- Forma de pago: {venta.forma_pago}')

                input('precione una tecla para continuar!')
    except TecStoreError as e:
        input(e)



#   _________________
#|--| Listar Ventas |-----------------------------------------------------
def listar_ventas():
    ventas = Gestion_Venta().extraer_ventas()
    print('|# Lista de Ventas')
    if ventas:
        for venta in ventas:
            print(venta)
        input('precione una tecla para continuar!')
    else: 
        print('|  ·No se emcontraron ventas!')
        input('precione una tecla para continuar!')
        return
