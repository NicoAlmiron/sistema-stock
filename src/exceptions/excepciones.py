class TecStoreError(Exception):
    mensaje_default = "|· Ocurrio un error inesperado!"

    def __init__(self, mensaje = None, dni = None):
        self.mensaje = mensaje or self.mensaje_default
        self.dni = dni or None
        super().__init__(self.mensaje)

    def __str__(self):
        return self.mensaje

class DatoInvalidoError(TecStoreError):
    mensaje_default = "|· El dato ingresado es invalido"

class DniRegistrado(TecStoreError):
    def __init__(self, mensaje=None, dni=None):
        super().__init__(mensaje, dni)
    mensaje_default = "|· Este DNI ya se encuentra registrado"

class DatoNumericoObligatorio(TecStoreError):
    mensaje_default = "|· Debe ingresar solo valores numericos"

class OpcionInvalida(TecStoreError):
    mensaje_default = "|· Ingrese una opcion valida!"

class AuthenticationError(TecStoreError):
    mensaje_default = '|·· *ERROR* - USUARIO Y/O  |\n| CONTRASEÑA INCORRECTOS ··|'

class ClavesDistintaError(TecStoreError):
    mensaje_default = '|· Las contraseñas deben ser iguales'

class NombreInvalido(TecStoreError):
    mensaje_default = '|· Debe ser un Nombre valido (max 30 caracteres)'

class OperacionCancelada(TecStoreError):
    mensaje_default = '|· Se cancelo la operacion'

class PrecioDemaciadoAlto(TecStoreError):
    mensaje_default = '|· El Precio exedio el limite permitido (limite $99.999.999.999)'

class PrecioNegativoError(TecStoreError):
    mensaje_default = '|· El Precio no puede ser negativo!'

class NumeroDemasiadoAlto(TecStoreError):
    mensaje_default = '|· Numero demaciado alto!'

class NumeroNegativoError(TecStoreError):
    mensaje_default = '|· El numero NO puede ser Negativo'

class ArchivoVacio(TecStoreError):
    mensaje_default = '|· Sin Registros '

class StockInsuficiente(TecStoreError):
    mensaje_default = '|· Producto Sin Stock!'


class UsuarioActivo(TecStoreError):
    mensaje_default = '|· Este Usuario Ya Se Encuentra Activo!'

class UsuarioSuspendido(TecStoreError):
    mensaje_default = '|· Este Usuario Ya Se Encuentra Suspendido!'

class VentaCancelada():
    mensaje_default = '|· Se cancelo la venta!'




