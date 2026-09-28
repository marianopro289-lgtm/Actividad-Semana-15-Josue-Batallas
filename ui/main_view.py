import tkinter as tk
from tkinter import ttk, messagebox
import os

from PIL import Image, ImageTk


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.ruta_assets = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "assets"
        )

        self.crear_interfaz()

    def crear_interfaz(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # -------------------------
        # LOGO
        # -------------------------
        ruta_logo = os.path.join(self.ruta_assets, "logo.png")

        if os.path.exists(ruta_logo):
            try:
                imagen = Image.open(ruta_logo)
                imagen = imagen.resize((80, 80))
                self.logo = ImageTk.PhotoImage(imagen)

                tk.Label(
                    self.frame,
                    image=self.logo
                ).pack(pady=(10, 0))

            except Exception:
                pass

        # -------------------------
        # TITULO
        # -------------------------
        titulo = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=5)

        subtitulo = tk.Label(
            self.frame,
            text="Panel principal"
        )
        subtitulo.pack()

        # -------------------------
        # NAVEGACION
        # -------------------------
        navegacion = tk.Frame(self.frame)
        navegacion.pack(pady=15)

        tk.Button(
            navegacion,
            text="Productos",
            width=18,
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            navegacion,
            text="Usuarios",
            width=18,
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            navegacion,
            text="Ventas",
            width=18,
            command=self.mostrar_ventas
        ).grid(row=0, column=2, padx=5)

        # -------------------------
        # INFORMACION
        # -------------------------
        self.info_label = tk.Label(
            self.frame,
            text=""
        )
        self.info_label.pack(pady=10)

        # -------------------------
        # CONTENEDOR PRINCIPAL
        # -------------------------
        self.contenido = tk.Frame(self.frame)
        self.contenido.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        # -------------------------
        # CERRAR SESION
        # -------------------------
        tk.Button(
            self.frame,
            text="Cerrar sesión",
            width=20,
            command=self.cerrar_sesion
        ).pack(pady=10)

        self.actualizar_informacion()

    # =========================================================
    # INFORMACION
    # =========================================================

    def actualizar_informacion(self):
        self.info_label.config(
            text=(
                f"Usuarios registrados: "
                f"{self.servicio.cantidad_usuarios()}    |    "
                f"Productos registrados: "
                f"{self.servicio.cantidad_productos()}"
            )
        )

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    # =========================================================
    # PRODUCTOS
    # =========================================================

    def mostrar_productos(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Productos",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=5)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("codigo", "nombre", "precio", "stock"),
            show="headings",
            height=8
        )

        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")
        tabla.heading("stock", text="Stock")

        tabla.column("codigo", width=100)
        tabla.column("nombre", width=180)
        tabla.column("precio", width=100)
        tabla.column("stock", width=100)

        tabla.pack(fill="x", pady=5)

        for producto in self.servicio.listar_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.precio,
                    producto.stock
                )
            )

    # =========================================================
    # USUARIOS
    # =========================================================

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=5)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("identificacion", "nombre"),
            show="headings",
            height=8
        )

        tabla.heading(
            "identificacion",
            text="Identificación"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.column(
            "identificacion",
            width=150
        )

        tabla.column(
            "nombre",
            width=250
        )

        tabla.pack(fill="x", pady=5)

        for usuario in self.servicio.listar_usuarios():
            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre
                )
            )

    # =========================================================
    # VENTAS
    # =========================================================

    def mostrar_ventas(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Registro de ventas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=5)

        # -------------------------
        # SELECCION DE USUARIO
        # -------------------------
        tk.Label(
            self.contenido,
            text="Usuario:"
        ).pack(pady=(5, 2))

        usuarios = self.servicio.listar_usuarios()

        usuarios_opciones = [
            f"{usuario.identificacion} - {usuario.nombre}"
            for usuario in usuarios
        ]

        usuario_combo = ttk.Combobox(
            self.contenido,
            values=usuarios_opciones,
            state="readonly",
            width=40
        )

        usuario_combo.pack(pady=3)

        # -------------------------
        # SELECCION DE PRODUCTO
        # -------------------------
        tk.Label(
            self.contenido,
            text="Producto:"
        ).pack(pady=(5, 2))

        productos = self.servicio.listar_productos()

        productos_opciones = [
            f"{producto.codigo} - {producto.nombre}"
            for producto in productos
            if producto.stock > 0
        ]

        producto_combo = ttk.Combobox(
            self.contenido,
            values=productos_opciones,
            state="readonly",
            width=40
        )

        producto_combo.pack(pady=3)

        # -------------------------
        # CALLBACK DE VENTA
        # -------------------------
        def registrar_venta():
            usuario_seleccionado = usuario_combo.get()
            producto_seleccionado = producto_combo.get()

            if not usuario_seleccionado:
                messagebox.showwarning(
                    "Venta",
                    "Seleccione un usuario."
                )
                return

            if not producto_seleccionado:
                messagebox.showwarning(
                    "Venta",
                    "Seleccione un producto."
                )
                return

            identificacion_usuario = (
                usuario_seleccionado.split(" - ")[0]
            )

            codigo_producto = (
                producto_seleccionado.split(" - ")[0]
            )

            exito, mensaje = self.servicio.registrar_venta(
                identificacion_usuario,
                codigo_producto
            )

            if exito:
                messagebox.showinfo(
                    "Venta",
                    mensaje
                )

                self.actualizar_informacion()
                self.mostrar_ventas()

            else:
                messagebox.showerror(
                    "Venta",
                    mensaje
                )

        # -------------------------
        # BOTON
        # -------------------------
        tk.Button(
            self.contenido,
            text="Registrar venta",
            width=20,
            command=registrar_venta
        ).pack(pady=10)

        # -------------------------
        # TABLA DE VENTAS
        # -------------------------
        tabla = ttk.Treeview(
            self.contenido,
            columns=("usuario", "producto", "fecha"),
            show="headings",
            height=6
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.heading(
            "producto",
            text="Producto"
        )

        tabla.heading(
            "fecha",
            text="Fecha"
        )

        tabla.column(
            "usuario",
            width=130
        )

        tabla.column(
            "producto",
            width=130
        )

        tabla.column(
            "fecha",
            width=180
        )

        tabla.pack(
            fill="x",
            pady=5
        )

        for venta in self.servicio.listar_ventas():
            tabla.insert(
                "",
                "end",
                values=(
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )