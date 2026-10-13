from src.utils.Helpers import limpiar_consola, lista_Clases_a_diccionario
from .Producto_services import listar_productos, mostrar_un_prod, descontar_stock
from src.persistensia.Ventas_JSON import extraer_ventas, escribir_venta
from src.persistensia.Productos_JSON import escribir_productos, extraer_productos

from src.classes import Venta, DetalleVenta


metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")

#|--------  VENTAS  --------|#
#   __________________
#|--| Realizar Venta |-----------------------------------------------------
def realizar_venta(vendedor):

    productos = extraer_productos()

    descuento = False

    venta = Venta(None,None,None,None,vendedor.id_usuario)

    list_prods = []

    total_venta = 0

    while True:
        id_prod_v = None
        limpiar_consola()
        print('|###--··  TecStore  ··--###|')
        listar_productos(productos)
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        if len(list_prods) > 0:
            print('||||-Carrito:')
            for i, prod in enumerate(list_prods):
                print(f'||-{prod.nombre.upper()} x {prod.cantidad}')
            print(f'||\t\t\t·Total: ${total_venta:,}')
            print('|---------------------------------------------------------------------------')
        print('|-· Ingrese el Id del producto (Dejar vacio para continuar)')
        id_prod_v = input('|##-· ID: ')

        if id_prod_v == '':
            break        

        for i, producto in enumerate(productos):
            if int(id_prod_v) == producto.id_producto:
                cant = 0
                cant_str = ""
                cant_str = input('|##-· Cantidad: ')
                if cant_str == "":
                    cant = 1
                else:
                    cant = int(cant_str)
                if producto.stock > 0 and producto.stock >= cant:

                    det_prod_ven = DetalleVenta(None, None, None, None, None, None)

                    det_prod_ven.id_producto = producto.id_producto
                    det_prod_ven.nombre = producto.nombre
                    det_prod_ven.precio = producto.precio
                    det_prod_ven.stock = producto.stock
                    det_prod_ven.cantidad = cant
                    det_prod_ven.subtotal = producto.precio * cant
                    
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
                else:
                    print('|# Producto Sin Stock')
                    input('precione una tecla para continuar!')
                    break
                print(f'|\t-{producto.nombre.upper()} x {cant} Agregado a la compra') 
                input('precione una tecla para continuar!')

    venta.importe_total = total_venta

    if list_prods:
        lista_ventas = extraer_ventas()
        id_new = len(lista_Clases_a_diccionario(lista_ventas)) + 1
        venta.id_venta = id_new
        venta.detalle_venta = list_prods

        while True:
            limpiar_consola()
            print('|###--··  TecStore  ··--###|')

            for i,prod in enumerate(list_prods):
                nom_prod = prod.nombre.upper()
                cant_prod = prod.cantidad
                sub_total_prod = prod.subtotal

                print(f'|-{nom_prod}{" " * (30 - len(nom_prod))} x {cant_prod} - ${sub_total_prod:,}')
            
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
                venta['importe_total'] = float(venta.importe_total)-(float(venta.importe_total)*(desc/100))
                print(f'|-----------Importe Total ${total_venta:,} ')
                print(f'|-----------Importe con Descuento ${venta.importe_total:,} ')
                descuento = True
                break
            elif opc == "2":
                desc = float(input('|#  ·Descuento: $ '))
                venta.importe_total = venta.importe_total - desc
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

        venta.detalle_venta = list_prods

        ventas = []
        ventas = extraer_ventas()
        ventas.append(venta)
        escribir_venta(ventas)
        escribir_productos(productos)
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



#   _________________
#|--| Listar Ventas |-----------------------------------------------------
def listar_ventas():
    ventas = extraer_ventas()
    print('|# Lista de Ventas')
    if ventas:
        for venta in ventas:
            print(venta)
        input('precione una tecla para continuar!')
    else: 
        print('|  ·No se emcontraron ventas!')
        input('precione una tecla para continuar!')
        return
