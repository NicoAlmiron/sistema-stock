import csv
from src.exceptions.excepciones import ErrorPersistencia


class ExportadorCSV:
    ENCABEZADO = ["id_venta", "fecha", "cliente", "vendedor", "producto", "cantidad",
                  "precio_unitario", "subtotal", "metodo_pago", "descuento", "total_venta"]

    def __init__(self, ruta="ventas_historial.csv"):
        self.ruta = ruta

    def exportar_ventas(self, ventas):
        # Una fila por cada producto vendido. El descuento y el total de la venta
        # se escriben solo en la primera fila de cada venta, asi la columna se puede sumar.
        try:
            with open(self.ruta, "w", newline="", encoding="utf-8-sig") as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                escritor.writerow(self.ENCABEZADO)
                for venta in ventas:
                    primera_fila = True
                    for detalle in venta.detalle_venta:
                        if primera_fila:
                            descuento = venta.desc_monto or 0
                            total = venta.importe_total
                        else:
                            descuento = ""
                            total = ""
                        escritor.writerow([
                            venta.id_venta,
                            venta.fecha.strftime("%d/%m/%Y %H:%M:%S"),
                            venta.cliente,
                            venta.vendedor_nombre,
                            detalle.nombre,
                            detalle.cantidad,
                            detalle.precio,
                            detalle.subtotal,
                            venta.forma_pago,
                            descuento,
                            total])
                        primera_fila = False
        except OSError:
            raise ErrorPersistencia("No se pudo escribir " + self.ruta + " (esta abierto en otro programa?)")
        return len(ventas)