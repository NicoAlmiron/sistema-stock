class TecStoreError(Exception):
    mensaje_default = "|· Ocurrio un error inesperado!"

    def __init__(self, mensaje = None):
        self.mensaje = mensaje or self.mensaje_default
        super().__init__(self.mensaje)

    def __str__(self):
        return self.mensaje

class DatoInvalidoError(Exception):
    mensaje_default = "|· El dato ingresado es invalido"

class DniRegistrado(Exception):
    mensaje_default = "|· Este DNI ya se encuentra registrado"

class DatoNumericoObligatorio(Exception):
    mensaje_default = "|· Debe ingresar solo valores numericos"

class OpcionInvalida(Exception):
    mensaje_default = "|· Ingrese una opcion valida!"