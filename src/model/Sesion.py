from .Usuario import Usuario
from datetime import datetime

#print(ahora.strftime("%d/%m/%Y"))           # 12/10/2026
#print(ahora.strftime("%H:%M"))              # 19:05
#print(ahora.strftime("%d/%m/%Y %H:%M:%S"))  # 12/10/2026 19:05:32

class Sesion(Usuario):
    def __init__(self, id_usuario, nombre, dni, telefono, rol, id_sesion, sal=None, hash= None, fecha_alta = None, fecha_baja = None, prods_vendidos = None, monto_bruto = None, inicio_actividad=None, fin_actividad = None, monto_neto = None):
        super().__init__(id_usuario, nombre, dni, telefono, rol, sal, hash, fecha_alta, fecha_baja)
        self.id_sesion = id_sesion
        self.inicio_actividad = inicio_actividad if inicio_actividad is not None else datetime.now()
        self.prods_vendidos = prods_vendidos 
        self.monto_bruto = monto_bruto 
        self.monto_neto = monto_neto 
        self.fin_actividad = fin_actividad 

    def to_dict(self):
        diccionario = {
            "id_sesion" : self.id_sesion,
            "id_usuario" : self.id_usuario,
            "nombre" : self.nombre,
            "dni" : self.dni,
            "telefono" : self.telefono,
            "rol" : self.rol,
            "inicio_actividad" : str(self.inicio_actividad),
            "prods_vendidos" : self.prods_vendidos,
            "monto_bruto" : self.monto_bruto,
            "monto_neto" : self.monto_neto,
            "fin_actividad" : str(self.fin_actividad)
        }
        return diccionario 

    def from_dict(self, user_sesion):
        sesion = Sesion(
            id_sesion = int(user_sesion['id_sesion']),
            id_usuario = int(user_sesion['id_usuario']),
            nombre = user_sesion['nombre'],
            dni = user_sesion['dni'],
            telefono = user_sesion['telefono'],
            rol = user_sesion['rol'],
            inicio_actividad = user_sesion['inicio_actividad'],
            prods_vendidos = int(user_sesion['prods_vendidos']),
            monto_bruto = float(user_sesion['monto_bruto']),
            monto_neto = float(user_sesion['monto_neto']),
            fin_actividad = user_sesion['fin_actividad'] 
        )
        return sesion


    def verificar_permisos(self):
        if self.rol == "ADMINISTRADOR":
            return True
        elif self.rol == "EMPLEADO":
            return False    

    def cerrar_sesion(self, monto_bruto, prods_vendidos, monto_neto):
        self.prods_vendidos = prods_vendidos
        self.monto_bruto = monto_bruto 
        self.monto_neto = monto_neto 
        self.fin_actividad = datetime.now()
        
