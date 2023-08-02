import tkinter as tk
from controller.controlador_principal import ControladorPrincipal

root = tk.Tk()
root.title("Cactus world Tour")
controlador = ControladorPrincipal(root)
root.mainloop()
