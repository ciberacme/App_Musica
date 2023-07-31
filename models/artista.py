import json


class Artista:
    def __init__(self, evento, artista, genero, lugar, fecha):
        self.evento = evento
        self.artista = artista
        self.genero = genero
        self.lugar = lugar
        self.fecha = fecha

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**artista) for artista in data]