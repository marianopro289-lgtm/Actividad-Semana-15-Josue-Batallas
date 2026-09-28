import json
import os


class ArchivoServicio:

    def __init__(self):
        # Ubicación de la carpeta principal del proyecto
        self.carpeta_proyecto = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    def obtener_ruta(self, ruta):
        return os.path.join(
            self.carpeta_proyecto,
            ruta
        )

    def leer_json(self, ruta):
        ruta_completa = self.obtener_ruta(ruta)

        try:
            with open(
                ruta_completa,
                "r",
                encoding="utf-8"
            ) as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

    def guardar_json(self, ruta, datos):
        ruta_completa = self.obtener_ruta(ruta)

        with open(
            ruta_completa,
            "w",
            encoding="utf-8"
        ) as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )