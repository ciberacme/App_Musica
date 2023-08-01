import tkinter as tk
import os
from models.artista import Artista
from views1.vista_inicio import VistaInicio
from views1.vista_artistas import VistaArtistas
from views1.vista_info import VistaInfo
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_artistas import ControladorArtistas
from controllers.controlador_info import ControladorInfo


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Cactours La musica en tu camino")
        self.geometry("1200x800+400+300")
        self.resizable(True, True)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        artistas = Artista.cargar_de_json("data/artistas.json")

        controlador_inicio = ControladorInicio(self)
        controlador_artistas = ControladorArtistas(self, artistas)
        controlador_info = ControladorInfo(self)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_artistas = VistaArtistas(self, controlador_artistas)
        self.vista_info = VistaInfo(self, controlador_info)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_artistas)
        self.ajustar_frame(self.vista_info)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")
        #self.config(bg="#2F242C")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
        #self.config(bg="#2F242C")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
