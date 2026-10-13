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