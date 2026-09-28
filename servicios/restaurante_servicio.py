from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio
from datetime import datetime


class RestauranteServicio:

    def __init__(self):
        self.archivo_servicio = ArchivoServicio()

        self.usuarios = []
        self.productos = []
        self.ventas = []

        self.cargar_usuarios()
        self.cargar_productos()
        self.cargar_ventas()

    def cargar_usuarios(self):
        datos = self.archivo_servicio.leer_json("datos/usuarios.json")

        self.usuarios = [
            Usuario(
                usuario["identificacion"],
                usuario["nombre"],
                usuario["contrasena"]
            )
            for usuario in datos
        ]

    def cargar_productos(self):
        datos = self.archivo_servicio.leer_json("datos/productos.json")

        self.productos = [
            Producto(
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            )
            for producto in datos
        ]

    def cargar_ventas(self):
        datos = self.archivo_servicio.leer_json("datos/ventas.json")

        self.ventas = [
            Venta(
                venta["usuario"],
                venta["producto"],
                venta["fecha"]
            )
            for venta in datos
        ]

    def validar_acceso(self, identificacion, contrasena):
        for usuario in self.usuarios:
            if (
                usuario.identificacion == identificacion
                and usuario.contrasena == contrasena
            ):
                return True

        return False

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def listar_ventas(self):
        return self.ventas

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def registrar_producto(self, codigo, nombre, precio, stock):
        nuevo_producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self.productos.append(nuevo_producto)
        self.guardar_productos()

    def actualizar_producto(self, codigo, nombre, precio, stock):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.nombre = nombre
                producto.precio = precio
                producto.stock = stock

                self.guardar_productos()
                return True

        return False

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                self.guardar_productos()
                return True

        return False

    def guardar_productos(self):
        datos = []

        for producto in self.productos:
            datos.append({
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            })

        self.archivo_servicio.guardar_json(
            "datos/productos.json",
            datos
        )

    def registrar_venta(self, identificacion_usuario, codigo_producto):
        usuario_encontrado = None
        producto_encontrado = None

        for usuario in self.usuarios:
            if usuario.identificacion == identificacion_usuario:
                usuario_encontrado = usuario
                break

        for producto in self.productos:
            if producto.codigo == codigo_producto:
                producto_encontrado = producto
                break

        if usuario_encontrado is None:
            return False, "El usuario no existe."

        if producto_encontrado is None:
            return False, "El producto no existe."

        if producto_encontrado.stock <= 0:
            return False, "El producto no tiene stock disponible."

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_venta = Venta(
            usuario_encontrado.identificacion,
            producto_encontrado.codigo,
            fecha
        )

        self.ventas.append(nueva_venta)

        producto_encontrado.stock -= 1

        self.guardar_productos()
        self.guardar_ventas()

        return True, "Venta registrada correctamente."

    def guardar_ventas(self):
        datos = []

        for venta in self.ventas:
            datos.append({
                "usuario": venta.usuario,
                "producto": venta.producto,
                "fecha": venta.fecha
            })

        self.archivo_servicio.guardar_json(
            "datos/ventas.json",
            datos
        )