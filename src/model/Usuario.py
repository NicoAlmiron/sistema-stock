from datetime import datetime
from src.utils.Helpers import dar_formato_id, dar_formato_dni, dar_formato_nombre, dar_formato_telefono
from src.exceptions.excepciones import UsuarioActivo, UsuarioSuspendido, NombreInvalido, DatoInvalidoError

class Usuario:
    ROL_ADMIN = "ADMINISTRADOR"
    ROL_EMPLEADO = "EMPLEADO"
    ROLES = (ROL_ADMIN, ROL_EMPLEADO)
    NOMBRE_MAX = 30

    def __init__(self, id_usuario, nombre, dni, telefono, rol, sal, hash, fecha_alta = None, fecha_baja = ""):
        self._id_usuario = id_usuario
        self.nombre = nombre              # setter: valida
        self._dni = dni
        self.telefono = telefono
        self.rol = rol                    # setter: valida
        self._sal = sal
        self._hash = hash
        self.fecha_alta = fecha_alta if fecha_alta is not None else datetime.now()
        self.fecha_baja = fecha_baja

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def dni(self):
        return self._dni

    @property
    def sal(self):
        return self._sal

    @property
    def hash(self):
        return self._hash

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        valor = str(valor).strip()
        if not valor or len(valor) > self.NOMBRE_MAX:
            raise NombreInvalido()
        self._nombre = valor

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, valor):
        if valor not in self.ROLES:
            raise DatoInvalidoError("Rol invalido")
        self._rol = valor

    def verificar_permisos(self):
        return self.rol == self.ROL_ADMIN

    def __str__(self):
        linea  = f"|·ID: {self.id_usuario}{dar_formato_id(self.id_usuario)}"
        linea += f"|·NOMBRE: {self.nombre}{dar_formato_nombre(self.nombre)}"
        linea += f"|·DNI: {self.dni}{dar_formato_dni(self.dni)}"
        linea += f"|·TELEFONO: {self.telefono}{dar_formato_telefono(self.telefono)}"
        linea += "|· ACTIVO" if self.fecha_baja == "" else  f"|· SUSPENDIDO"

        return linea

    def to_dict(self):
        user_dict = {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "dni": self.dni,
            "telefono": self.telefono,
            "rol": self.rol,
            "sal": self.sal,
            "hash": self.hash,
            "fecha_alta": str(self.fecha_alta),
            "fecha_baja": str(self.fecha_baja) if self.fecha_baja else ""
        }
        return user_dict    

    @classmethod
    def from_dict(cls, user):
        return cls(
            id_usuario = int(user["id_usuario"]),
            nombre = user["nombre"],
            dni = user["dni"],
            telefono = user["telefono"],
            rol = user["rol"],
            sal = user["sal"],
            hash = user["hash"],
            fecha_alta = user["fecha_alta"],
            fecha_baja = "" if user["fecha_baja"] == "" else user["fecha_baja"]
        )
        
    

    def validar_estado(self):
        return not self.fecha_baja          # activo = sin fecha de baja

    def baja_usuario(self):
        if not self.validar_estado():
            raise UsuarioSuspendido()
        self.fecha_baja = datetime.now()

    def reactivacion_usuario(self):
        if self.validar_estado():
            raise UsuarioActivo()
        self.fecha_baja = ""