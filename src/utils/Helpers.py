import os
import hmac
import hashlib
from src.exceptions.excepciones import DatoNumericoObligatorio, OpcionInvalida, ClavesDistintaError, NombreInvalido, OperacionCancelada, PrecioDemaciadoAlto, PrecioNegativoError, NumeroDemasiadoAlto, NumeroNegativoError

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
#lo anterior se realiza para poder limpiar la consola

def pausar_consola(mensaje=None):
    cadena = mensaje if mensaje is not None else "Presione Enter para continuar..."
    sobrante = 80 - len(cadena)
    
    izq = sobrante // 2             # división entera (redondea para abajo)
    der = sobrante - izq            # lo que queda va a la derecha
    
    input(f'|#····{" " * izq}{cadena}{" " * der}····#|')

def guion_base(cadena=""):
    caracteres = len(cadena) if cadena is not None else 0
    lon = 90 - caracteres
    linea = f'|{cadena}{" "*lon}|'
    print(linea)
    return linea

def guion_opcion(num, cadena):
    caracteres = len(cadena) if cadena is not None else 0
    lon = 51 - caracteres
    linea = f'|{" "*31}{num} ) --- {cadena}{" "*lon}|'
    print(linea)
    return linea

def guion_titulo(cadena=""):
    cadena = cadena if cadena is not None else ""        
    sobrante = 80 - len(cadena)

    izq = sobrante // 2             # división entera (redondea para abajo)                           INICIO DE SESION 
    der = sobrante - izq            # lo que queda va a la derecha

    linea = f'|#····{" " * izq}{cadena}{" " * der}····#|'
    print(linea)
    return linea

def guion_item(cadena=None):
    caracteres = len(cadena) if cadena is not None else 0
    lon = 68 - caracteres
    linea = f'|#{"·"*20}> {cadena}{(" " * lon)}···#|'
    print(linea)
    return linea

def guion_sub_item(cadena=None):
    caracteres = len(cadena) if cadena is not None else 0
    lon = 68 - caracteres
    linea = f'| {" "*15} ·>{cadena}{(" " * lon)}···#|'
    print(linea)
    return linea

def cabecera_menu() -> None:
    print(f'|###--··{" "*34}TecStore{" "*34}··--###|')
    print(f'|##··········{" "*66}··········##|')

def pedir_opcion(op):
    if op == "":
        raise OperacionCancelada()
    elif not op.isdigit():
        raise DatoNumericoObligatorio()
    elif len(op) >= 5:
        raise NumeroDemasiadoAlto()
    elif int(op) < 0:
        raise OpcionInvalida()
    else:
        return op


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


def pedir_id(id):
    if id == "": 
        raise OperacionCancelada() 
    elif not id.isdigit():
        raise DatoNumericoObligatorio()
    elif len(id) >= 12:
        raise NumeroDemasiadoAlto()
    elif int(id) < 0:
        raise NumeroNegativoError() 
    else:
        return int(id)
    
def venta_pedir_id(id):
    if id == "": 
        return 0
    elif not id.isdigit():
        raise DatoNumericoObligatorio()
    elif len(id) >= 12:
        raise NumeroDemasiadoAlto()
    elif int(id) < 0:
        raise NumeroNegativoError() 
    else:
        return int(id)

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
    elif not precio.isdigit():
        raise DatoNumericoObligatorio()
    elif len(precio) >= 12:
        raise PrecioDemaciadoAlto()
    elif float(precio) < 0:
        raise PrecioNegativoError() 
    else:
        return float(precio)

def pedir_stock(stock):
    if stock == "":
        raise OperacionCancelada()
    elif not stock.isdigit():
        raise DatoNumericoObligatorio()
    elif len(stock) >= 5:
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
    return (" " * ( 30 - len(str(nombre)) ) )

def dar_formato_precio(precio_prod) -> None:
    return (" " * ( 13 - len(precio_prod)))

def dar_formato_dni(dni) -> None:
    return (" " * ( 10 - len(str(dni)) ) )

def dar_formato_telefono(telefono) -> None:
    return (" " * ( 10 - len(str(telefono)) ) )


def auto_descuento(importe, descuento_porcentual = None, descuento_importe = None):
    descuento = descuento_importe if descuento_importe is None else descuento_porcentual
    if descuento_importe is not None:
        return importe - descuento_importe
    else :
        return float(importe) - (float(importe)*(descuento/100))




