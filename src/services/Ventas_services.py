from src.utils.Helpers import (limpiar_consola, cabecera_menu, venta_pedir_id, pedir_stock, pedir_precio,
                               guion_base, pedir_opcion, pausar_consola, guion_item, guion_titulo, pedir_cantidad,
                               dar_formato_nombre, dar_formato_precio)
from .Producto_services import descontar_stock, listar_productos
from src.persistensia.Gestion_Producto import Gestion_Producto
from src.persistensia.Gestion_Venta import Gestion_Venta
from src.persistensia.ExportadorCSV import ExportadorCSV
from src.exceptions.excepciones import (TecStoreError, VentaCancelada, OperacionCancelada, OpcionInvalida,
                                        NombreInvalido, IdNoEncontrado, MetodoPagoInvalidoError, ArchivoVacio)
from src.model.Venta import Venta
from src.model.Detalle_Producto import Detalle_Producto




#|--------  VENTAS  --------|#
#   __________________
#|--| Realizar Venta |-----------------------------------------------------
def realizar_venta(vendedor):
 
    productos = Gestion_Producto().extraer_productos()
 
    try:
        prod_vent = pasarela_produtos()
        list_prods = prod_vent["lista_productos"]
        productos = prod_vent["productos"]
 
        if not list_prods:
            raise OperacionCancelada()
 
        venta = Venta(id_venta=Gestion_Venta().definir_id(),
                      id_vendedor=vendedor.id_usuario,
                      vendedor_nombre=vendedor.nombre,
                      detalles=list_prods)
        limpiar_consola()
        cabecera_menu()
        guion_item('FINALICE LA VENTA')
        listar_carrito(list_prods, venta)
 
        venta.cliente = ingresar_cliente()
        venta.forma_pago = pasarela_metodos_pago()
        venta.aplicar_descuento_efectivo()          # 10% si paga en efectivo
        limpiar_consola()
        cabecera_menu()
        listar_carrito(list_prods, venta)
        if vendedor.verificar_permisos():
            aplicar_descuentos_venta(venta)         # el admin puede reemplazarlo por uno especial
 
        if Gestion_Venta().procesar_venta(venta):
            Gestion_Producto().escribir_productos(productos)
            guion_titulo('Se realizo la venta exitosamente!')
            pausar_consola()
            limpiar_consola()
            mostrar_resumen_venta(venta)
        else:
            raise TecStoreError()
    except TecStoreError as e:
        pausar_consola(e.mensaje)



#   _________________
#|--| Listar Ventas |-----------------------------------------------------
def listar_ventas():
    
    hist_ventas = Gestion_Venta().extraer_ventas()
    guion_titulo('HISTORIAL DE VENTAS')
    if hist_ventas:
        for det_venta in hist_ventas:
            print(det_venta)
        pausar_consola()
    else: 
        guion_titulo('No se encontraron ventas!')
        pausar_consola()
        return


def pasarela_produtos():
    total_venta = 0 
    list_prods = []
    productos = Gestion_Producto().extraer_productos()
    while True:
        limpiar_consola()
        cabecera_menu()
        guion_titulo('REALIZAR VENTA')
        guion_base()
        listar_productos(productos)
        guion_base()
        print(f'|{"|"*90}|')
        if list_prods:
            print(f'|--->    Carrito:{" "*74}|')
            for prod in list_prods:
                print(prod)
            guion_base()
            print(f'|##······{" "*32}·Total: ${total_venta:,}{" "*(40 - len(str(total_venta)))}|')
            print(f'|{"-"*90}|')
        print(f'|-· Ingrese el Id del producto (Dejar vacio para continuar){" "*32}|')
        try:
            id_prod_v = venta_pedir_id(input('|##-· ID: '))  
            encontrado = False
        
            if id_prod_v == 0:
                return {
                            "lista_productos" : list_prods, 
                            "productos" : productos
                        }
            else:
                for i, producto in enumerate(productos):
                    if id_prod_v == producto.id_producto and not producto.discontinuado:
                        encontrado = True
                        cant = pedir_cantidad(input('|##-· Cantidad: '))
                        if producto.verificar_stock(cant):

                            det_prod_ven = Detalle_Producto(
                                id_producto=producto.id_producto,
                                nombre = producto.nombre,
                                precio=producto.precio,
                                cantidad=cant
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
                        guion_base()
                        print(f'|{" "*15}-{producto.nombre.upper()} x {cant} Agregado a la compra!{" " * (49 - (len(producto.nombre) + len(str(cant))))}|') 
                        guion_base()
                        pausar_consola()
                if not encontrado:
                    raise IdNoEncontrado()
        except TecStoreError as er:
            pausar_consola(er.mensaje)


def pasarela_metodos_pago():
    metodos_pago = ("Efectivo", "Transferencia", "Tarjeta")
    guion_item('FORMA DE PAGO      (introduzca el numero de la forma de pago)')
    print(f'|· ( 1 ) Efectivo · ( 2 ) Transferencia · ( 3 ) Tarjeta · ( 0 ) Cancelar{" "*19}|')
    guion_base()
    op =  pedir_opcion(input('|#######-Forma de Pago: '))
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
            raise MetodoPagoInvalidoError()


def aplicar_descuentos_venta(venta):
    guion_item('APLICAR DESCUENTOS')
    print(f'|· ( 1 ) % Porcentaje · ( 2 ) $ Importe · ( 0 ) Sin Descuentos{" "*29}|')
    opc = pedir_opcion(input('|##-Opcion: '))
                                    
    if opc == "1":
        venta.descuento_porcentaje(pedir_stock(input('|#  ·Descuento: % ')))
        print(f'|-----------Importe Total ${venta.importe_sin_desc:,}{" "*(64-len(str(venta.importe_sin_desc)))}|')
        print(f'|-----------Importe con Descuento ${venta.importe_total:,}{" "*(56-len(str(venta.importe_total)))}|')
        return venta
    elif opc == "2":
        venta.descuento_importe(pedir_precio(input('|#  ·Descuento: $ ')))
        print(f'|-----------Importe Total ${venta.importe_sin_desc:,}{" "*(64-len(str(venta.importe_sin_desc)))}|')
        print(f'|-----------Importe con Descuento ${venta.importe_total:,}{" "*(56-len(str(venta.importe_total)))}|')
        return venta
    elif opc in ("0", ""):
        print(f'|-----------Importe Actual ${venta.importe_total:,}{" "*(63-len(str(venta.importe_total)))}|')
        return venta
    else:
        raise OpcionInvalida()


def ingresar_cliente():
    guion_item('Ingresar Cliente')
    cliente = input('|##- Cliente: ')
    if cliente == "":
        return ""
    elif len(cliente) > 30:
        raise NombreInvalido()
    else:
        return cliente


def listar_carrito(lista_prods, venta):
    for prod in lista_prods:
        print(prod)          
    guion_base()
    print(f'|\n|{"-" * 40} Total: ${venta.importe_sin_desc:,}{" "* (39-len(str(venta.importe_sin_desc)))}|')


def mostrar_resumen_venta(venta):
    guion_item("RESUMEN DE LA VENTA")
    print('|-- Productos')
    for prod in venta.detalle_venta:
        precio = f'{prod.precio:,}'
        linea = f"|    + {prod.nombre.upper()}{dar_formato_nombre(prod.nombre)}"
        linea += f'${precio}{dar_formato_precio(precio)} C/U'
        linea += f' x {prod.cantidad} - ${prod.subtotal:,}{" " * (28 - (len(str(prod.cantidad))+len(str(prod.subtotal))) )}|'
        print(linea)
    print(f'|-- Total: ${venta.importe_sin_desc:,}{" "*(79-(len(str(venta.importe_sin_desc))))}|')
    if venta.descuento_tipo:
        print(f'|-- Descuento: -${venta.desc_monto:,}{" "*(73-(len(str(venta.desc_monto))))}|')
        print(f'|-- Total Neto(Descuento): ${venta.importe_total:,}{" "*(62-(len(str(venta.importe_total))))}|')
    print(f'|-- Forma de pago: {venta.forma_pago}{" "*(71-(len(str(venta.forma_pago))))}|')
    pausar_consola()

def exportar_historial_csv():
    cabecera_menu()
    ventas = Gestion_Venta().extraer_ventas()
    if not ventas:
        raise ArchivoVacio('No hay ventas para exportar')
    cantidad = ExportadorCSV().exportar_ventas(ventas)
    pausar_consola("Se exportaron " + str(cantidad) + " ventas a ventas_historial.csv")