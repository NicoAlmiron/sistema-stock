import json
from src.classes.Usuario import Usuario
from datetime import datetime
#from src.utils.Helpers import lista_Clases_a_diccionario

ARCHIVO_USUARIO_JSON = "src/data/usuarios.json"


def extraer_usuarios(): 
    try:
        usuarios = [] 
        with open(ARCHIVO_USUARIO_JSON , 'r', encoding='UTF-8') as users_json:

            lista_users = json.load(users_json)
            if len(lista_users) == 0:
                return []
            
            for user in lista_users:
                usuario = Usuario(
                    id_usuario = int(user["id_usuario"]),
                    nombre = user["nombre"],
                    dni = user["dni"],
                    telefono = user["telefono"],
                    rol = user["rol"],
                    sal = user["sal"],
                    hash = user["hash"],
                    fecha_alta = user["fecha_alta"],
                    productos_vendidos = int(user["productos_vendidos"]),
                    importe_vendido = float(user["importe_vendido"]),
                    fecha_baja = "" if user["fecha_baja"] is "" else user["fecha_baja"]
                )

                usuarios.append(usuario)
        return usuarios
    except FileNotFoundError:
        #input("Archivo Json no encontrado!")
        return []
    except:
        return []




def escribir_usuarios(usuarios):
    lista_dicc = []
    for user in usuarios:
        lista_dicc.append(user.a_dict())
    try:

        with open(ARCHIVO_USUARIO_JSON , 'w', encoding='UTF-8') as users_json:
            arch_json = json.dumps(
                lista_dicc,
                indent=4)
            users_json.write(arch_json)
            return True
    except FileNotFoundError:
        with open(ARCHIVO_USUARIO_JSON , 'w', encoding='UTF-8') as users_json:
            arch_json = json.dumps(
                lista_dicc,
                indent=4)
            users_json.write(arch_json)
            return True
    except FileExistsError:
        input("A sucedido un error inesperado!")
        return False
    
    