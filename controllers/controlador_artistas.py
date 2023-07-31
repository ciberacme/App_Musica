class ControladorArtistas:
    def __init__(self, app, modelo_artista):
        self.app = app
        self.modelo_artista = modelo_artista

    def obtener_artistas(self):
        return self.modelo_artista

    def seleccionar_artista(self):
        """
        Obtiene el índice del artistas seleccionado y llama a la vista de
        información para mostrar la información de los eventos.
        """
        indice = self.app.vista_artistas.obtener_artista_seleccionado()
        if indice is not None:
            artista = self.modelo_artista[indice]
            self.app.vista_info.mostrar_info_artista(artista)
            self.app.cambiar_frame(self.app.vista_info)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)