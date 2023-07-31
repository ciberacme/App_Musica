import tkinter as tk


class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un juego.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.artista_label = tk.Label(self, text="")
        self.artista_label.pack(pady=50)
        self.artista_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar a la lista de artistas",
            command=self.controlador.regresar_artistas,
        )
        self.boton_regresar.pack(pady=10)

    def mostrar_info_artista(self, artista):
        """
        Muestra la información del juego recibido como parámetro.
        """
        info = f"Evento: {artista.evento}\nArtista: {artista.artista}\nGénero: {artista.genero}\nLugar: {artista.lugar}\nFecha: {artista.fecha}"
        self.artista_label["text"] = info
