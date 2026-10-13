class TecStoreError(Exception):
    mensaje_default = "|· Ocurrio un error inesperado!"

    def __init__(self, mensaje = None):
        self.mensaje = mensaje or self.mensaje_default
        super().__init__(self.mensaje)

    def __str__(self):
        return self.mensaje

class DatoInvalidoError(TecStoreError):
    mensaje_default = "|· El dato ingresado es invalido"

class DniRegistrado(TecStoreError):
    mensaje_default = "|· Este DNI ya se encuentra registrado"

class DatoNumericoObligatorio(TecStoreError):
    mensaje_default = "|· Debe ingresar solo valores numericos"

class OpcionInvalida(TecStoreError):
    mensaje_default = "|· Ingrese una opcion valida!"

class AuthenticationError(TecStoreError):
    mensaje_default = f'|·· *ERROR* - USUARIO Y/O  |\n| CONTRASEÑA INCORRECTOS ··|'

class ClavesDistintaError(TecStoreError):
    mensaje_default = f'|· Las contraseñas deben ser iguales'

class NombreInvalido(TecStoreError):
    mensaje_default = f'|· Debe ser un Nombre valido (max 30 caracteres)'

class OperacionCancelada(TecStoreError):
    mensaje_default = f'|· Se cancelo la operacion'

class PrecioDemaciadoAlto(TecStoreError):
    mensaje_default = f'|· El Precio exedio el limite permitido (limite $99.999.999.999)'

class PrecioNegativoError(TecStoreError):
    mensaje_default = f'|· El Precio no puede ser negativo!'

class NumeroDemasiadoAlto(TecStoreError):
    mensaje_default = f'|· Numero demaciado alto!'

class NumeroNegativoError(TecStoreError):
    mensaje_default = f'|· El numero NO puede ser Negativo'

