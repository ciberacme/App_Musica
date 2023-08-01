import tkinter as tk
from tkinter.font import Font

class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=32, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Tour de Musica", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=5)

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo2 = tk.Label(self, text="Noroeste del Pais", font=titulo_font)
        self.titulo2.grid(padx=0, pady=0)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=16)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Aquí puedes ver los eventos que te ofrecemos. Por genero, lugar y disponibilidad de localidades y mucho mas... solo para ustedes nuestros queridos clientes",
            font=descripcion_font,
            wraplength=400,
        )
        self.descripcion.grid(row=2, column=0, padx=10 ,pady=50)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Aquí puedes ver los eventos que te ofrecemos. Por genero, lugar y disponibilidad de localidades y mucho mas... solo para ustedes nuestros queridos clientes",
            font=descripcion_font,
            wraplength=400,
        )
        self.descripcion.grid(row=3, column=2, padx=10 ,pady=50)

        # Crea el botón para ir a juegos y lo agrega a la vista
        self.boton_artistas = tk.Button(self, text="Ir a Eventos", command=self.controlador.mostrar_artistas)
        self.boton_artistas.grid(row=3, column=0, pady=10)
        
        # Crea el botón 2 para ir a juegos y lo agrega a la vista
        self.boton_artistas = tk.Button(self, text="Ir a Eventos", command=self.controlador.mostrar_artistas)
        self.boton_artistas.grid(row=4, column=2, pady=10)
