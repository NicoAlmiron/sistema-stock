import json
from src.exceptions.excepciones import ErrorPersistencia


class GestorJSON:

    def __init__(self, ruta):
        self.ruta = ruta

    def leer(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []                      
        except json.JSONDecodeError:
            raise ErrorPersistencia("El archivo " + self.ruta + " esta danado")

    def guardar(self, datos):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
        return True