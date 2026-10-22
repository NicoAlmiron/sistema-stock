from datetime import datetime
from .Usuario import Usuario


class Sesion:
    def __init__(self, usuario, id_sesion, inicio_actividad=None, prods_vendidos=None,
                 monto_bruto=None, monto_neto=None, fin_actividad=None):
        self._usuario = usuario
        self.id_sesion = id_sesion
        self.inicio_actividad = inicio_actividad if inicio_actividad is not None else datetime.now()
        self.prods_vendidos = prods_vendidos
        self.monto_bruto = monto_bruto
        self.monto_neto = monto_neto
        self.fin_actividad = fin_actividad

    # Lo que el resto del programa le pregunta a la sesion se lo pasa al usuario
    @property
    def usuario(self):
        return self._usuario

    @property
    def id_usuario(self):
        return self._usuario.id_usuario

    @property
    def nombre(self):
        return self._usuario.nombre

    @property
    def dni(self):
        return self._usuario.dni

    @property
    def telefono(self):
        return self._usuario.telefono

    @property
    def rol(self):
        return self._usuario.rol

    def verificar_permisos(self):
        return self._usuario.verificar_permisos()

    def cerrar_sesion(self, monto_bruto, prods_vendidos, monto_neto):
        self.prods_vendidos = prods_vendidos
        self.monto_bruto = monto_bruto
        self.monto_neto = monto_neto
        self.fin_actividad = datetime.now()

    def to_dict(self):
        return {
            "id_sesion": self.id_sesion,
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "dni": self.dni,
            "telefono": self.telefono,
            "rol": self.rol,
            "inicio_actividad": str(self.inicio_actividad),
            "prods_vendidos": self.prods_vendidos,
            "monto_bruto": self.monto_bruto,
            "monto_neto": self.monto_neto,
            "fin_actividad": str(self.fin_actividad)
        }

    @classmethod
    def from_dict(cls, user_sesion):
        # En el historial solo queda una copia de los datos del usuario de ese momento
        usuario = Usuario(
            id_usuario=int(user_sesion['id_usuario']),
            nombre=user_sesion['nombre'],
            dni=user_sesion['dni'],
            telefono=user_sesion['telefono'],
            rol=user_sesion['rol'],
            sal=None,
            hash=None)
        return cls(
            usuario=usuario,
            id_sesion=int(user_sesion['id_sesion']),
            inicio_actividad=user_sesion['inicio_actividad'],
            prods_vendidos=int(user_sesion['prods_vendidos']),
            monto_bruto=float(user_sesion['monto_bruto']),
            monto_neto=float(user_sesion['monto_neto']),
            fin_actividad=user_sesion['fin_actividad'])