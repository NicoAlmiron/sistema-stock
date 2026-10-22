from datetime import datetime, date, time, timedelta
from src.persistensia.Gestion_Venta import Gestion_Venta
from src.persistensia.Gestion_Producto import Gestion_Producto
from src.exceptions.excepciones import TecStoreError, OpcionInvalida, OperacionCancelada
from src.utils.Helpers import (limpiar_consola, cabecera_menu, guion_titulo, guion_item,
                               guion_base, guion_opcion, pedir_opcion, pausar_consola)

STOCK_BAJO = 4   # mismo criterio que Producto.__str__ (stock bajo = menos de 4)


#|--------  CALCULOS (no imprimen nada, reciben datos y devuelven datos)  --------|#

def _bruto(venta):
    # Se calcula desde las lineas del detalle: es lo que realmente se vendio.
    return float(sum(d.subtotal for d in venta.detalle_venta))


def _neto(venta):
    # Una venta sin descuento puede traer importe_total en None (la venta 8 del historial).
    # En ese caso no hubo descuento y el neto es igual al bruto.
    if venta.importe_total is not None:
        return float(venta.importe_total)
    return _bruto(venta)


def _descuento(venta):
    # Se deduce de bruto - neto, asi tambien aparecen los descuentos de ventas viejas
    # que no guardaron desc_monto (la venta 2 tiene 10% aplicado sin registrarlo).
    return _bruto(venta) - _neto(venta)


def resumen_general(ventas):
    cant = len(ventas)
    neto = sum(_neto(v) for v in ventas)
    return {
        "ventas": cant,
        "unidades": sum(d.cantidad for v in ventas for d in v.detalle_venta),
        "bruto": sum(_bruto(v) for v in ventas),
        "descuentos": sum(_descuento(v) for v in ventas),
        "neto": neto,
        "ventas_con_descuento": sum(1 for v in ventas if _descuento(v) > 0.005),
        "ticket_promedio": neto / cant if cant else 0.0,
    }


def por_forma_pago(ventas):
    datos = {}
    for v in ventas:
        fila = datos.setdefault(v.forma_pago, {"forma": v.forma_pago, "ventas": 0, "monto": 0.0})
        fila["ventas"] += 1
        fila["monto"] += _neto(v)
    return sorted(datos.values(), key=lambda f: f["monto"], reverse=True)


def por_producto(ventas):
    # Se agrupa por id (el nombre se puede editar despues). "facturado" es antes del
    # descuento, porque el descuento se aplica a la venta completa y no a cada producto.
    datos = {}
    for v in ventas:
        for d in v.detalle_venta:
            fila = datos.setdefault(d.id_producto, {"id": d.id_producto, "nombre": d.nombre,
                                                    "unidades": 0, "facturado": 0.0})
            fila["nombre"] = d.nombre
            fila["unidades"] += d.cantidad
            fila["facturado"] += d.subtotal
    return list(datos.values())


def top_productos(ventas, por="unidades", top=5):
    return sorted(por_producto(ventas), key=lambda p: p[por], reverse=True)[:top]


def por_vendedor(ventas):
    # El nombre del vendedor ya viaja dentro de cada venta, no hace falta cruzar con usuarios.
    datos = {}
    for v in ventas:
        fila = datos.setdefault(v.id_vendedor, {"id": v.id_vendedor, "nombre": v.vendedor_nombre,
                                                "ventas": 0, "unidades": 0, "neto": 0.0, "descuentos": 0.0})
        fila["ventas"] += 1
        fila["unidades"] += sum(d.cantidad for d in v.detalle_venta)
        fila["neto"] += _neto(v)
        fila["descuentos"] += _descuento(v)
    return sorted(datos.values(), key=lambda f: f["neto"], reverse=True)


def por_dia(ventas):
    datos = {}
    for v in ventas:
        dia = v.fecha.date()
        fila = datos.setdefault(dia, {"dia": dia, "ventas": 0, "neto": 0.0})
        fila["ventas"] += 1
        fila["neto"] += _neto(v)
    return [datos[d] for d in sorted(datos)]


def alertas_stock(productos, ventas):
    activos = [p for p in productos if not p.discontinuado]
    vendidos = {d.id_producto for v in ventas for d in v.detalle_venta}
    return {
        "sin_stock": [p for p in activos if p.stock == 0],
        "stock_bajo": [p for p in activos if 0 < p.stock < STOCK_BAJO],
        "sin_ventas": [p for p in activos if p.id_producto not in vendidos],
        "valor_inventario": sum(p.precio * p.stock for p in activos),
    }


#|--------  PERIODO  --------|#

def elegir_periodo():
    guion_item('PERIODO A CONSULTAR')
    guion_opcion("1", "Todo el historial")
    guion_opcion("2", "Hoy")
    guion_opcion("3", "Ultimos 7 dias")
    guion_opcion("4", "Este mes")
    guion_opcion("0", "Volver")
    op = pedir_opcion(input(f'|{" "*31}OPCION···---: '))

    inicio_hoy = datetime.combine(date.today(), time.min)
    match op:
        case "1":
            return "Todo el historial", datetime.min
        case "2":
            return "Hoy", inicio_hoy
        case "3":
            return "Ultimos 7 dias", inicio_hoy - timedelta(days=6)
        case "4":
            return "Este mes", inicio_hoy.replace(day=1)
        case "0":
            raise OperacionCancelada()
        case _:
            raise OpcionInvalida()


#|--------  PANTALLAS (solo imprimen)  --------|#

def _m(monto):
    return f'${monto:,.2f}'


def _barra(parte, total, ancho=20):
    return "#" * round(parte / total * ancho) if total else ""


def mostrar_resumen(ventas):
    r = resumen_general(ventas)
    guion_item('RESUMEN GENERAL')
    guion_base(f'   Ventas realizadas ........ {r["ventas"]}')
    guion_base(f'   Unidades vendidas ........ {r["unidades"]}')
    guion_base(f'   Total bruto .............. {_m(r["bruto"])}')
    guion_base(f'   Descuentos otorgados ..... -{_m(r["descuentos"])}  ({r["ventas_con_descuento"]} ventas con descuento)')
    guion_base(f'   Total neto (cobrado) ..... {_m(r["neto"])}')
    guion_base(f'   Ticket promedio .......... {_m(r["ticket_promedio"])}')


def mostrar_formas_pago(ventas):
    total = sum(_neto(v) for v in ventas)
    guion_item('POR FORMA DE PAGO')
    for f in por_forma_pago(ventas):
        pct = f["monto"] / total * 100 if total else 0
        guion_base(f'   {f["forma"]:<14}{f["ventas"]:>4} ventas  {_m(f["monto"]):>18}  {pct:5.1f}%  {_barra(f["monto"], total)}')


def mostrar_top_productos(ventas):
    guion_item('PRODUCTOS MAS VENDIDOS (por unidades)')
    for i, p in enumerate(top_productos(ventas, "unidades"), 1):
        guion_base(f'   {i}. {p["nombre"].upper():<30} x {p["unidades"]}')
    guion_base()
    guion_item('PRODUCTOS QUE MAS FACTURAN (antes de descuento)')
    for i, p in enumerate(top_productos(ventas, "facturado"), 1):
        guion_base(f'   {i}. {p["nombre"].upper():<30} {_m(p["facturado"]):>18}')


def mostrar_vendedores(ventas):
    guion_item('POR VENDEDOR')
    for f in por_vendedor(ventas):
        guion_base(f'   {f["nombre"]:<16}{f["ventas"]:>4} ventas  {f["unidades"]:>4} un.  {_m(f["neto"]):>18}  desc: {_m(f["descuentos"])}')


def mostrar_por_dia(ventas):
    dias = por_dia(ventas)
    mayor = max(d["neto"] for d in dias) if dias else 0
    guion_item('VENTAS POR DIA')
    for d in dias[-31:]:
        guion_base(f'   {d["dia"].strftime("%d/%m/%Y")}{d["ventas"]:>4} ventas  {_m(d["neto"]):>18}  {_barra(d["neto"], mayor)}')
    if len(dias) > 31:
        guion_base('   (se muestran los ultimos 31 dias)')


def mostrar_alertas_stock(ventas):
    a = alertas_stock(Gestion_Producto().extraer_productos(), ventas)

    def nombres(lista):
        return ", ".join(f'{p.nombre} ({p.stock})' for p in lista) or "ninguno"

    guion_item('ALERTAS DE STOCK')
    guion_base(f'   Sin stock ................ {nombres(a["sin_stock"])}')
    guion_base(f'   Stock bajo (menos de {STOCK_BAJO}) .. {nombres(a["stock_bajo"])}')
    guion_base(f'   Sin ventas en el periodo . {", ".join(p.nombre for p in a["sin_ventas"]) or "ninguno"}')
    guion_base(f'   Valor del inventario ..... {_m(a["valor_inventario"])}  (a precio de venta)')


#|--------  MENU  --------|#

def menu_estadisticas(usuario):
    # El administrador ve todo el negocio. El empleado ve solo sus propias ventas.
    es_admin = usuario.verificar_permisos()
    id_vendedor = None if es_admin else usuario.id_usuario

    periodo = None
    while True:
        limpiar_consola()
        cabecera_menu()
        try:
            if periodo is None:
                periodo = elegir_periodo()
                continue

            nombre_periodo, desde = periodo
            guion_titulo('ESTADISTICAS')
            guion_titulo(f'Periodo: {nombre_periodo}' + ('' if es_admin else f'  -  Ventas de {usuario.nombre}'))
            guion_titulo('')
            guion_opcion("1", "Resumen general")
            guion_opcion("2", "Formas de pago")
            guion_opcion("3", "Productos mas vendidos")
            if es_admin:
                guion_opcion("4", "Ventas por vendedor")
            guion_opcion("5", "Ventas por dia")
            guion_opcion("6", "Alertas de stock")
            guion_opcion("7", "Cambiar periodo")
            guion_opcion("0", "Volver")

            op = pedir_opcion(input(f'|{" "*31}OPCION···---: '))
            if op == "0":
                break
            if op == "7":
                periodo = None
                continue
            if op == "4" and not es_admin:
                raise OpcionInvalida()
            if op not in ("1", "2", "3", "4", "5", "6"):
                raise OpcionInvalida()

            limpiar_consola()
            cabecera_menu()
            ventas = Gestion_Venta().extraer_ventas_en_rango(desde, id_vendedor=id_vendedor)
            if not ventas and op != "6":
                guion_titulo('No hay ventas en este periodo')
            else:
                match op:
                    case "1":
                        mostrar_resumen(ventas)
                    case "2":
                        mostrar_formas_pago(ventas)
                    case "3":
                        mostrar_top_productos(ventas)
                    case "4":
                        mostrar_vendedores(ventas)
                    case "5":
                        mostrar_por_dia(ventas)
                    case "6":
                        mostrar_alertas_stock(ventas)
            guion_base()
            pausar_consola()

        except OperacionCancelada:
            if periodo is None:
                break          # cancelo la eleccion de periodo: vuelve al menu principal
        except TecStoreError as e:
            pausar_consola(e.mensaje)