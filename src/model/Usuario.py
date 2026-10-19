from datetime import datetime
from src.utils.Helpers import dar_formato_id, dar_formato_dni, dar_formato_nombre, dar_formato_telefono
from src.exceptions.excepciones import UsuarioActivo, UsuarioSuspendido

class Usuario():
    def __init__(self, id_usuario, nombre, dni, telefono, rol, sal, hash, fecha_alta = None, productos_vendidos = 0, importe_vendido = 0.0, fecha_baja = ""):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.rol = rol
        self.sal = sal
        self.hash = hash
        self.fecha_alta = fecha_alta if fecha_alta is not None else datetime.now()
        self.productos_vendidos = productos_vendidos
        self.importe_vendido = importe_vendido
        self.fecha_baja = fecha_baja


    def __str__(self):
        linea  = f"|·ID: {self.id_usuario}{dar_formato_id(self.id_usuario)}"
        linea += f"|·NOMBRE: {self.nombre}{dar_formato_nombre(self.nombre)}"
        linea += f"|·DNI: {self.dni}{dar_formato_dni(self.dni)}"
        linea += f"|·TELEFONO: {self.telefono}{dar_formato_telefono(self.telefono)}"
        linea += "|· ACTIVO" if self.fecha_baja == "" else  f"|· SUSPENDIDO"

        return linea

    def a_dict(self):
        user_dict = {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "dni": self.dni,
            "telefono": self.telefono,
            "rol": self.rol,
            "sal": self.sal,
            "hash": self.hash,
            "fecha_alta": str(self.fecha_alta),
            "productos_vendidos": self.productos_vendidos,
            "importe_vendido": self.importe_vendido,
            "fecha_baja": str(self.fecha_baja) if self.fecha_baja else ""
        }
        return user_dict    

    def validar_estado(self):
        if self.fecha_baja != "":
            return False
        elif self.fecha_baja == "":
            return True

    

    def baja_usuario(self):
        if self.fecha_baja is "" or None:
            self.fecha_baja = datetime.now()
        else:
            raise UsuarioActivo()

    def reactivacion_usuario(self):
        if self.fecha_baja:
            self.fecha_baja = ""
        else:
            raise UsuarioSuspendido()