from .Usuario import Usuario
from datetime import datetime

#print(ahora.strftime("%d/%m/%Y"))           # 12/10/2026
#print(ahora.strftime("%H:%M"))              # 19:05
#print(ahora.strftime("%d/%m/%Y %H:%M:%S"))  # 12/10/2026 19:05:32

class Sesion(Usuario):
    def __init__(self, id_usuario, nombre, dni, telefono, rol, id_sesion, sal=None, hash= None, fecha_alta = None, productos_vendidos = None, importe_vendido = None, fecha_baja = None, prods_vendidos = None, monto_bruto = None, inicio_activididad=None, fin_actividad = None):
        super().__init__(id_usuario, nombre, dni, telefono, rol, sal, hash, fecha_alta, productos_vendidos, importe_vendido, fecha_baja)
        self.id_sesion = id_sesion
        self.inicio_activididad = inicio_activididad if inicio_activididad is not None else datetime.now()
        self.prods_vendidos = prods_vendidos 
        self.monto_bruto = monto_bruto 
        self.fin_actividad = fin_actividad 

    def to_dict(self):
        diccionario = {
            "id_sesion" : self.id_sesion,
            "id_usuario" : self.id_usuario,
            "nombre" : self.nombre,
            "dni" : self.dni,
            "telefono" : self.telefono,
            "rol" : self.rol,
            "inicio_activididad" : str(self.inicio_activididad),
            "prods_vendidos" : self.prods_vendidos,
            "monto_bruto" : self.monto_bruto,
            "fin_actividad" : str(self.fin_actividad)
        }
        return diccionario 

    def verificar_permisos(self):
        if self.rol == "ADMINISTRADOR":
            return True
        elif self.rol == "EMPLEADO":
            return False    

    def cerrar_sesion(self):
        self.prods_vendidos = 10 #cant_prod_vend(sesion)
        self.monto_bruto = 345000 #mon_tot_vend(sesion)
        self.fin_actividad = datetime.now()
        
