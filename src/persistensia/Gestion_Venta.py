from datetime import datetime
from src.model.Venta import Venta
from .Gestor_JSON import GestorJSON


class Gestion_Venta(GestorJSON):
    def __init__(self):
        super().__init__("src/data/historial_ventas.json")

    def extraer_ventas(self):
        ventas = []
        for dicc in self.leer():
            ventas.append(Venta.from_dict(dicc))
        return ventas

    def procesar_venta(self, venta_nueva):
        lista = []
        for venta in self.extraer_ventas():
            lista.append(venta.to_dict())
        lista.append(venta_nueva.to_dict())
        return self.guardar(lista)

    def definir_id(self):
        ventas = self.extraer_ventas()
        if not ventas:
            return 1
        return max(v.id_venta for v in ventas) + 1


    def extraer_ventas_en_rango(self, desde, hasta=None, id_vendedor=None):
        hasta = hasta if hasta is not None else datetime.now() # si no trae el "hasta" pone el momento actual

        return [
            v for v in self.extraer_ventas()    
            
            if desde <= v.fecha <= hasta 
            and (id_vendedor is None or v.id_vendedor == id_vendedor) 
        ]