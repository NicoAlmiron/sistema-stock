import os
import hmac
import hashlib
from src.exceptions.excepciones import DatoNumericoObligatorio, OpcionInvalida, ClavesDistintaError, NombreInvalido, OperacionCancelada, PrecioDemaciadoAlto, PrecioNegativoError, NumeroDemasiadoAlto, NumeroNegativoError

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola

def cabecera_menu() -> None:
    print('|###--··  TecStore  ··--###|')
    print('|##······················##|')

def pausar_consola():
    input("Presione Enter para continuar...")


def lista_Clases_a_diccionario(lista_clases):
    lista_diccionarios = []
    for clase in lista_clases:
        lista_diccionarios.append(clase.to_dict())
    return lista_diccionarios

def hashear_clave(clave):
    sal = os.urandom(16) # este es un valor aleatorio que se mezclara con la clave
    hash_clave = hashlib.pbkdf2_hmac("sha256", clave.encode(), sal, 100_000) #100_000 son las veces que se repite el calculo

    return sal.hex(), hash_clave.hex() #se pasan valores hex, que es como texto en json

def verificar_clave(clave_ingresada, sal_hex, hash_guardaro_hex):
    sal = bytes.fromhex(sal_hex)
    hash_ingresado = hashlib.pbkdf2_hmac("sha256", clave_ingresada.encode(), sal, 100_000)
    return hmac.compare_digest(hash_ingresado.hex(), hash_guardaro_hex) # compara y resuleve True o False


def pedir_nombre(nombre):
    if nombre == "":
        raise OperacionCancelada()
    elif len(nombre) > 30:
        raise NombreInvalido()
    else:
        return nombre


def pedir_telefono():
    while True:
        telefono = input('|#-TELEFONO: ')
        if not telefono.isdigit():
            raise DatoNumericoObligatorio()
        else:
            return telefono

def pedir_precio(precio):
    if precio == "": 
        raise OperacionCancelada() 
    elif len(precio) >= 12:
        raise PrecioDemaciadoAlto()
    elif float(precio) < 0:
        raise PrecioNegativoError() 
    else:
        return float(precio)

def pedir_stock(stock):
    if stock == "":
        raise OperacionCancelada()
    elif len(stock) >= 4:
        raise NumeroDemasiadoAlto()
    elif int(stock) < 0:
        raise NumeroNegativoError()
    else:
        return int(stock)

def definir_rol():
    while True:
        print('|#(1) EMPLEADO | (2) ADMIN #|')
        rol = input('|-ROL: ')
        if rol == "1" or rol.upper == "EMPLEADO":
            return "EMPLEADO"
        elif rol == "2" or rol.upper == "ADMIN" or rol.upper == "ADMINISTRADOR":
            return "ADMINISTRADOR"
        else:
            raise OpcionInvalida()
        
def definir_clave():
    while True:
        clave = input('|#-CONTRASEÑA: ')
        print('|# REPETIR CONTRASEÑA ')
        claveRep = input('|#-CONTRASEÑA: ')
        if clave == claveRep:
            return clave
        else:
            raise ClavesDistintaError()

def dar_formato_id(id) -> None:
    return (" " * ( 6 - len(str(id)) ) )

def dar_formato_nombre(nombre) -> None:
    return (" " * ( 30 - len(nombre) ) )

def dar_formato_precio(precio_prod) -> None:
    return (" " * ( 13 - len(precio_prod)))

def dar_formato_dni(dni) -> None:
    return (" " * ( 10 - len(str(dni)) ) )

def dar_formato_telefono(telefono) -> None:
    return (" " * ( 10 - len(str(telefono)) ) )




