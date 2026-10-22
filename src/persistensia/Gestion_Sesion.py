from src.model.Sesion import Sesion

from .Gestion_Venta import Gestion_Venta
from .Gestor_JSON import GestorJSON


class Gestion_Sesion(GestorJSON):
    def __init__(self):
        super().__init__("src/data/historial_actividad.json")

    def extraer_historial_actividad(self):
        historial = []
        for dicc in self.leer():
            historial.append(Sesion.from_dict(dicc))
        return historial

    def escribir_historial_actividad(self, sesion):
        lista = []
        for actividad in self.extraer_historial_actividad():
            lista.append(actividad.to_dict())
        lista.append(sesion.to_dict())
        return self.guardar(lista)

    def definir_id(self):
        hist_actv =  self.extraer_historial_actividad()

        if not hist_actv:
            return 1
        
        return max(h.id_sesion for h in hist_actv) + 1


    def crear_sesion(self, user):
        id_sesion = self.definir_id()
        sesion_activa = Sesion(usuario=user, id_sesion=id_sesion)
        return sesion_activa


    def guardar_sesion(self, sesion):
        ventas = Gestion_Venta().extraer_ventas_en_rango(desde=sesion.inicio_actividad,id_vendedor=sesion.id_usuario) #cant_prod_vend(sesion)
        sesion.cerrar_sesion(
            monto_bruto=sum(dv.subtotal for v in ventas for dv in v.detalle_venta),
            prods_vendidos=sum(dv.cantidad for v in ventas for dv in v.detalle_venta),
            monto_neto=sum(v.importe_total for v in ventas))
        self.escribir_historial_actividad(sesion)