# Restaurante App - Semana 15

## Programación Orientada a Objetos

**Nombre:** Josue Batallas  
**Actividad:** Semana 15  
**Proyecto:** restaurante_app

---

## 1. Descripción del proyecto

Este proyecto corresponde a la continuación del proyecto `restaurante_app` que se ha venido trabajando durante las semanas anteriores de la materia de Programación Orientada a Objetos.

En esta semana se continuó trabajando sobre la misma estructura del proyecto, sin empezar desde cero. Se mantuvieron las funciones que ya estaban realizadas y se agregó una nueva sección para poder registrar y visualizar las ventas realizadas.

El proyecto está desarrollado en Python utilizando una estructura modular, separando los modelos, servicios, datos y la interfaz gráfica.

La aplicación permite iniciar sesión, administrar productos y usuarios, y ahora también registrar ventas desde la interfaz gráfica.

---

## 2. Objetivo de la Semana 15

El objetivo principal de esta semana fue agregar el manejo de ventas al proyecto que ya se tenía realizado.

Para esto se implementó:

- Un nuevo modelo llamado `Venta`.
- Un archivo `ventas.json` para guardar las ventas.
- Una nueva sección de ventas en la interfaz.
- Selección de usuarios y productos existentes.
- Registro de una venta mediante un botón.
- Uso de `command=` y funciones callback para los botones.
- Comunicación entre la interfaz y `RestauranteServicio`.
- Guardado de las ventas en un archivo JSON.
- Visualización de las ventas registradas mediante una tabla.
- Uso de imágenes y logotipo dentro de la interfaz mediante la carpeta `assets`.

---

## 3. Evolución del proyecto

El proyecto se fue desarrollando por etapas. En las semanas anteriores ya se había creado la estructura principal de la aplicación, el inicio de sesión, la administración de productos y la administración de usuarios.

Para esta semana se mantuvo esa estructura y se agregó el módulo de ventas.

De esta manera, no se tuvo que crear nuevamente todo el proyecto, sino que se continuó trabajando sobre lo que ya estaba realizado.

La nueva funcionalidad se integró a las partes que ya existían para mantener el proyecto organizado y evitar mezclar las responsabilidades de cada archivo.

---

## 4. Estructura del proyecto

La estructura principal del proyecto quedó organizada de la siguiente manera:

```text
restaurante_app/
│
├── assets/
│   ├── logo.png
│   ├── productos.png
│   ├── usuarios.png
│   └── ventas.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
