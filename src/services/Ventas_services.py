from src.utils.Helpers import limpiar_consola, cabecera_menu, venta_pedir_id, pedir_stock, pedir_precio
from src.utils.Helpers import auto_descuento, pedir_nombre
from .Producto_services import  descontar_stock
from src.persistensia.Gestion_Producto import Gestion_Producto
from src.persistensia.Gestion_Venta import Gestion_Venta
from src.exceptions.excepciones import TecStoreError, VentaCancelada, OperacionCancelada, OpcionInvalida, NombreInvalido
from src.model.Venta import Venta
from src.model.Detalle_Producto import Detalle_Producto
from src.model.Detalle_Venta import Detalle_Venta




#|--------  VENTAS  --------|#
#   __________________
#|--| Realizar Venta |-----------------------------------------------------
def realizar_venta(vendedor):

    productos = Gestion_Producto().extraer_productos()

    descuento = False

    venta = Venta(id_venta = None,forma_pago = None, importe_total= None, fecha = None)

    list_prods = []

    try:
        prod_vent = pasarela_produtos()
        print(prod_vent)
        list_prods = prod_vent["lista_productos"]
        venta.importe_sin_desc = prod_vent["importe_total"]
        productos = prod_vent["productos"]

        if list_prods:
            venta.id_venta = Gestion_Venta().definir_id()
            limpiar_consola()
            print('|###--··  TecStore  ··--###|')

            for prod in list_prods:
                    print(prod)          
            print(f'|\n|{"-" * 31}Total: ${venta.importe_sin_desc:,}')

            cliente = ingresar_cliente()

            venta.forma_pago = pasarela_metodos_pago()

            if vendedor.verificar_permisos():
                descuento = True
                venta = aplicar_descuentos_venta(venta)
            else:
                venta.descuento_porcentaje(10)
            
            venta_completa = Detalle_Venta(
                            id_venta = venta.id_venta,
                            id_vendedor = vendedor.id_usuario, 
                            vendedor_nombre = vendedor.nombre,
                            cliente=cliente,
                            forma_pago = venta.forma_pago, 
                            importe_total = venta.importe_total, 
                            importe_sin_desc=venta.importe_sin_desc,
                            descuento_tipo=venta.descuento_tipo,
                            desc_monto=venta.desc_monto,
                            desc_tipo_importe=venta.desc_tipo_importe,
                            desc_tipo_porcentual=venta.desc_tipo_porcentual,
                            detalle_venta = list_prods
                            )
            #print(venta)
            if Gestion_Venta().procesar_venta(venta_completa):
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
                        
                print(f'|-- Total: ${venta.importe_sin_desc:,}')
                if descuento: 
                    print(f'|-- Descuento: -${venta.desc_monto}')
                    print(f'|-- Total Neto(Descuento): ${venta.importe_total}')
                print(f'|-- Forma de pago: {venta.forma_pago}')
                input('precione una tecla para continuar!')
            else: 
                raise TecStoreError()
        else:
            raise OperacionCancelada()
    except TecStoreError as e:
        input(e)



#   _________________
#|--| Listar Ventas |-----------------------------------------------------
def listar_ventas():
    
    hist_ventas = Gestion_Venta().extraer_ventas()
    print('|# Lista de Ventas')
    if hist_ventas:
        for det_venta in hist_ventas:
            print(det_venta)
        input('precione una tecla para continuar!')
    else: 
        print('|  ·No se encontraron ventas!')
        input('precione una tecla para continuar!')
        return


def pasarela_produtos():
    total_venta = 0 
    list_prods = []
    productos = Gestion_Producto().extraer_productos()
    while True:
        limpiar_consola()
        cabecera_menu()
        Gestion_Producto().listar_productos(productos)
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        if list_prods:
            print('||||-Carrito:')
            for prod in list_prods:
                print(prod)
            print(f'||\t\t\t·Total: ${total_venta:,}')
            print('|---------------------------------------------------------------------------')
        print('|-· Ingrese el Id del producto (Dejar vacio para continuar)')
        id_prod_v = venta_pedir_id(input('|##-· ID: '))  

        if id_prod_v == 0:
            return {
                        "lista_productos" : list_prods, 
                        "importe_total": total_venta,
                        "productos" : productos
                    }

        for i, producto in enumerate(productos):
            if id_prod_v == producto.id_producto:
                cant = 0
                cant = pedir_stock(input('|##-· Cantidad: '))
                if producto.verificar_stock(cant):

                    det_prod_ven = Detalle_Producto(
                        id_producto=producto.id_producto,
                        nombre = producto.nombre,
                        precio=producto.precio,
                        cantidad=cant,
                        subtotal = producto.precio * cant
                    )

                                    
                    total_venta = total_venta + (producto.precio * cant)

                    productos = descontar_stock(productos,producto.id_producto,cant)

                    nuevoProd = True

                    if list_prods:
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


def pasarela_metodos_pago():
    metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")
    print('|##-· Forma de pago')
    print('|· (1) Efectivo · (2) Transferencia · (3) Tarjeta · (0) Cancelar')
    op =  input('|##-Forma de Pago: ')
    match op:
        case '1':
            return metodos_pago[int(op)-1]
        case '2':
            return metodos_pago[int(op)-1]
        case '3':
            return metodos_pago[int(op)-1]
        case "0":
            raise VentaCancelada()
        case "":
            raise VentaCancelada()
        case _:
            raise OperacionCancelada()


def aplicar_descuentos_venta(venta):
    print('|##-· Aplicar descuentos')
    print('|· ( 1 ) % Porcentaje · ( 2 ) $ Importe · ( 0 ) Sin Descuentos')
    #imp_bruto = venta.importe_total
    opc = input('|##-Opcion: ')
                                    
    if opc == "1":
        venta.descuento_porcentaje(pedir_stock(input('|#  ·Descuento: % ')))
        print(f'|-----------Importe Total ${venta.importe_sin_desc:,} ')
        print(f'|-----------Importe con Descuento ${venta.importe_total:,} ')
        return venta
    elif opc == "2":
        venta.descuento_importe(pedir_precio(input('|#  ·Descuento: $ ')))
        print(f'|-----------| Importe Total ${venta.importe_sin_desc:,} ')
        print(f'|-----------| Importe con Descuento ${venta.importe_total:,} ')
        return venta
    elif opc == "0":
        print(f'|-----------Importe Actual ${venta.importe_total:,}')
        return venta
    elif opc == "":
        print(f'|-----------Importe Actual ${venta.importe_total:,}')
        return venta
    else:
        raise OpcionInvalida()


def ingresar_cliente():
    print('|##-· Ingresar Cliente')
    cliente = input('|##-Cliente: ')
    if cliente == "":
        return ""
    elif len(cliente) > 30:
        raise NombreInvalido()
    else:
        return cliente