from datetime import datetime
from src.exceptions.excepciones import NumeroDemasiadoAlto, NumeroNegativoError, MetodoPagoInvalidoError
from .Detalle_Producto import Detalle_Producto


class Venta:
    METODOS_PAGO = ("Efectivo", "Transferencia", "Tarjeta")
    DESCUENTO_EFECTIVO = 10   

    def __init__(self, id_venta, id_vendedor, vendedor_nombre, cliente=None, forma_pago=None,
                 fecha=None, detalles=None, descuento_tipo=None, descuento_valor=None):
        self.id_venta = id_venta
        self.id_vendedor = id_vendedor
        self.vendedor_nombre = vendedor_nombre
        self.cliente = cliente if cliente is not None else ""
        self._forma_pago = None
        if forma_pago is not None:
            self.forma_pago = forma_pago              # pasa por el setter, que valida
        self.fecha = fecha if fecha is not None else datetime.now()
        self._detalles = list(detalles) if detalles else []
        self._descuento_tipo = descuento_tipo          # None, "PORCENTUAL" o "IMPORTE"
        self._descuento_valor = descuento_valor

    # ---------- forma de pago ----------
    @property
    def forma_pago(self):
        return self._forma_pago

    @forma_pago.setter
    def forma_pago(self, valor):
        if valor not in self.METODOS_PAGO:
            raise MetodoPagoInvalidoError()
        self._forma_pago = valor

    # ---------- detalle (composicion: la venta TIENE lineas) ----------
    @property
    def detalle_venta(self):
        return tuple(self._detalles)      # solo lectura: para agregar se usa agregar_detalle

    def agregar_detalle(self, detalle):
        for d_prod in self._detalles:
            if d_prod.id_producto == detalle.id_producto:
                d_prod.cantidad += detalle.cantidad     # mismo producto: suma unidades
                return
        self._detalles.append(detalle)

    # ---------- importes (se calculan, no se guardan aparte) ----------
    @property
    def importe_sin_desc(self):
        return float(sum(d.subtotal for d in self._detalles))

    @property
    def descuento_tipo(self):
        return self._descuento_tipo

    @property
    def desc_tipo_porcentual(self):
        return self._descuento_valor if self._descuento_tipo == "PORCENTUAL" else None

    @property
    def desc_tipo_importe(self):
        return self._descuento_valor if self._descuento_tipo == "IMPORTE" else None

    @property
    def desc_monto(self):
        if self._descuento_tipo == "PORCENTUAL":
            return self.importe_sin_desc * self._descuento_valor / 100
        if self._descuento_tipo == "IMPORTE":
            return float(self._descuento_valor)
        return None

    def calcular_total_con_descuento(self):
        return self.importe_sin_desc - (self.desc_monto or 0)

    @property
    def importe_total(self):
        return self.calcular_total_con_descuento()

    # ---------- descuentos ----------
    def descuento_importe(self, descuento):
        if descuento < 0:
            raise NumeroNegativoError()
        if descuento > self.importe_sin_desc:
            raise NumeroDemasiadoAlto()
        self._descuento_tipo = "IMPORTE"
        self._descuento_valor = descuento

    def descuento_porcentaje(self, descuento):
        if descuento < 0:
            raise NumeroNegativoError()
        if descuento > 100:
            raise NumeroDemasiadoAlto()
        self._descuento_tipo = "PORCENTUAL"
        self._descuento_valor = descuento

    def quitar_descuento(self):
        self._descuento_tipo = None
        self._descuento_valor = None

    def aplicar_descuento_efectivo(self):
        if self.forma_pago == "Efectivo" and self._descuento_tipo is None:
            self.descuento_porcentaje(self.DESCUENTO_EFECTIVO)


    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_vendedor": self.id_vendedor,
            "vendedor_nombre": self.vendedor_nombre,
            "cliente": self.cliente,
            "forma_pago": self.forma_pago,
            "importe_sin_desc": self.importe_sin_desc,
            "descuento_tipo": self.descuento_tipo,
            "desc_monto": self.desc_monto,
            "desc_tipo_importe": self.desc_tipo_importe,
            "desc_tipo_porcentual": self.desc_tipo_porcentual,
            "importe_total": self.importe_total,
            "fecha": str(self.fecha),
            "detalle_venta": [d.to_dict() for d in self._detalles]
        }


    @classmethod
    def from_dict(cls, venta):
        tipo = venta["descuento_tipo"]
        if tipo == "PORCENTUAL":
            valor = venta["desc_tipo_porcentual"]
        elif tipo == "IMPORTE":
            valor = venta["desc_tipo_importe"]
        else:
            tipo, valor = None, None
        return cls(
            id_venta=int(venta["id_venta"]),
            id_vendedor=int(venta["id_vendedor"]),
            vendedor_nombre=venta["vendedor_nombre"],
            cliente=venta["cliente"],
            forma_pago=venta["forma_pago"],
            fecha=datetime.fromisoformat(venta["fecha"]),
            detalles=[Detalle_Producto.from_dict(d) for d in venta["detalle_venta"]],
            descuento_tipo=tipo,
            descuento_valor=float(valor) if valor is not None else None)


    def __str__(self):
        linea = f'|{"-"*17}> VENTA NRO: {self.id_venta}{" "* (60-len(str(self.id_venta)))}|'
        linea += f'\n|{" "*15} ·> Cajero: {self.vendedor_nombre}{" "* (63-len(self.vendedor_nombre))}|'
        linea += f'\n|{" "*15} ·> Fecha: {self.fecha.strftime("%d/%m/%Y %H:%M:%S")}{" "* (64-len(self.fecha.strftime("%d/%m/%Y %H:%M:%S")))}|'
        linea += f'\n|{" "*15} ·> Cliente: {self.cliente}{" "* (62-len(self.cliente))}|'
        linea += f'\n|{" "*15} ·>Forma de Pago: {self.forma_pago}{" "*(57-len(self.forma_pago))}|'
        linea += f'\n|{" "*15} ·>Total Bruto: ${self.importe_sin_desc:,}{" "*(57-len(str(self.importe_sin_desc)))}|'
        if self.descuento_tipo:
            if self.descuento_tipo == "PORCENTUAL":
                linea += f'\n|{" "*15} ·> Descuento: %{self.desc_tipo_porcentual}{" "*(59-(len(str(self.desc_tipo_porcentual))))}|'
            else:
                linea += f'\n|{" "*15} ·> Importe de Descuento{" "* 51}|'
            linea += f'\n|{" "*15} ·> descontado: -${self.desc_monto:,}{" "* (56-len(str(self.desc_monto)))}|'
            linea += f'\n|{" "*15} ·> Total Neto: ${self.importe_total:,}{" "* (57-len(str(self.importe_total)))}|'
        linea += f'\n|{" "*10}·> PRODUCTOS{" " * 68}|'
        for d in self._detalles:
            precio = f'{d.precio:,}'
            linea += f'\n|{" "*10}·{d.nombre}{" " * (30 - len(d.nombre))}'
            linea += f' - ${precio}{" " * (11 - len(precio))}'
            linea += f'- x {d.cantidad} - SubTotal ${d.subtotal:,}'
            linea += f'{" " * (16 - (len(str(d.cantidad)) + len(str(d.subtotal))))}|'
        linea += f'\n|##{"·"*20}{" "*46}{"·"*20}##|'
        return linea