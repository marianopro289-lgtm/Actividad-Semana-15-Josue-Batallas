import tkinter as tk
import os

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self, root):
        self.root = root

        # Asegurar que el programa trabaje desde la carpeta del proyecto
        carpeta_proyecto = os.path.dirname(os.path.abspath(__file__))
        os.chdir(carpeta_proyecto)

        self.root.title("Restaurante App")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.servicio = RestauranteServicio()

        self.mostrar_login()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_ventana()

        LoginView(
            self.root,
            self.servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self):
        self.limpiar_ventana()

        MainView(
            self.root,
            self.servicio,
            self.mostrar_login
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = RestauranteApp(root)

    root.mainloop()