import tkinter as tk


class VistaArtistas(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la lista de Artistas.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.artista = tk.Label(self, text="Lista de Eventos")
        self.artista.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        # Asocia el evento de doble clic a la función seleccionar_artista
        self.listbox.bind("<Double-Button-1>", self.seleccionar_artista)

        self.listbox.pack(pady=10)
        self.actualizar_artistas()

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)

    def actualizar_artistas(self):
        """
        Actualiza la lista de juegos con los Artistas obtenidos del controlador.
        """
        artistas = self.controlador.obtener_artistas()
        self.listbox.delete(0, tk.END)
        for artista in artistas:
            self.listbox.insert(tk.END, artista.artista)

    def obtener_artista_seleccionado(self):
        """
        Retorna el índice de los eventos seleccionados en la lista.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_artista(self, event):
        """
        Obtiene el índice de los eventos seleccionados y llama al controlador para
        mostrar la información del artista.
        """
        self.controlador.seleccionar_artista()
