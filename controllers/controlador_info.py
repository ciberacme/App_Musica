class ControladorInfo:
    def __init__(self, app):
        self.app = app

    def regresar_artistas(self):
        self.app.cambiar_frame(self.app.vista_artistas)
