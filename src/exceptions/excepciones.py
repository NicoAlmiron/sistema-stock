class TecStoreError(Exception):
    mensaje_default = "Ocurrio un error inesperado!"

    def __init__(self, mensaje = None, dni = None):
        self.mensaje = mensaje or self.mensaje_default
        self.dni = dni or None
        super().__init__(self.mensaje)

    def __str__(self):
        return self.mensaje


class DniRegistrado(TecStoreError):
    def __init__(self, mensaje=None, dni=None):
        super().__init__(mensaje, dni)
    mensaje_default = "Este DNI ya se encuentra registrado"

class MetodoPagoInvalidoError(TecStoreError):
    mensaje_default = "Metodo de pago invalido (Efectivo, Transferencia o Tarjeta)"

class ValidacionError(TecStoreError):
    mensaje_default = "Dato invalido"

class DatoInvalidoError(ValidacionError):
    mensaje_default = "El dato ingresado es invalido"

class DatoNumericoObligatorio(ValidacionError):
    mensaje_default = "Debe ingresar solo valores numericos"

class OpcionInvalida(ValidacionError):
    mensaje_default = "Ingrese una opcion valida!"

class AuthenticationError(TecStoreError):
    mensaje_default = '**  USUARIO Y/O CONTRASEÑA INCORRECTOS  **'

class ClavesDistintaError(ValidacionError):
    mensaje_default = 'Las contraseñas deben ser iguales'

class NombreInvalido(ValidacionError):
    mensaje_default = 'Debe ser un Nombre valido (max 30 caracteres)'

class OperacionCancelada(TecStoreError):
    mensaje_default = 'Se cancelo la operacion'

class PrecioDemaciadoAlto(ValidacionError):
    mensaje_default = 'El Precio exedio el limite permitido (limite $99.999.999.999)'

class PrecioNegativoError(ValidacionError):
    mensaje_default = 'El Precio no puede ser negativo!'

class NumeroDemasiadoAlto(ValidacionError):
    mensaje_default = 'Numero demaciado alto!'

class NumeroNegativoError(ValidacionError):
    mensaje_default = 'El numero NO puede ser Negativo'

class ArchivoVacio(TecStoreError):
    mensaje_default = 'Sin Registros '

class StockInsuficiente(ValidacionError):
    mensaje_default = 'Producto Sin Stock!'


class UsuarioActivo(TecStoreError):
    mensaje_default = 'Este Usuario Ya Se Encuentra Activo!'

class UsuarioSuspendido(TecStoreError):
    mensaje_default = 'Este Usuario Ya Se Encuentra Suspendido!'

class VentaCancelada(TecStoreError):
    mensaje_default = 'Se cancelo la venta!'

class IdNoEncontrado(TecStoreError):
    mensaje_default = 'No se encontro el id buscado!'

class ErrorPersistencia(TecStoreError):
       mensaje_default = "No se pudo leer o guardar la informacion"




