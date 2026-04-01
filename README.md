#  UNIDAD 2 - COMPONENTES Y LIBRERÍAS

##  INTRODUCCIÓN

En esta unidad se estudian los componentes, paquetes y librerías dentro de la programación, los cuales son fundamentales para desarrollar software moderno. Estos elementos permiten reutilizar código, mejorar la organización del proyecto y facilitar el mantenimiento de las aplicaciones. Gracias a ellos, es posible dividir un sistema en partes más pequeñas, reutilizables y eficientes, lo cual reduce errores y mejora la productividad del programador.

---

##  2.1 DEFINICIÓN CONCEPTUAL DE COMPONENTES, PAQUETES Y LIBRERÍAS

###  Componentes

Un componente es una parte reutilizable de un sistema que cumple una función específica. Puede ser visual, como botones o tarjetas dentro de una interfaz gráfica, o no visual, como funciones o clases que contienen lógica del programa. Los componentes ayudan a evitar la repetición de código y permiten construir sistemas más organizados.

###  Paquetes

Un paquete es una forma de organizar clases o archivos dentro de carpetas. Su función principal es mantener el código estructurado, facilitando su lectura, mantenimiento y reutilización en proyectos grandes.

###  Librerías

Una librería es un conjunto de funciones o herramientas ya desarrolladas que se pueden utilizar dentro de un programa. Estas permiten ahorrar tiempo al evitar programar desde cero funcionalidades comunes como gráficos, interfaces o manejo de datos.

###  Ejemplo (Uso de librerías en Python)

```python
import flet as ft
import matplotlib.pyplot as plt
import random
```

Estas librerías permiten crear interfaces gráficas, generar gráficas y simular datos.

###  Imagen

<img width="354" height="71" alt="image" src="https://github.com/user-attachments/assets/c1c0570b-cb19-4da9-ae34-3fb1ce07fc2f" />


---

##  2.2 USO DE LIBRERÍAS PROPORCIONADAS POR EL LENGUAJE

###  Explicación

Los lenguajes modernos incluyen librerías que facilitan tareas como la creación de interfaces gráficas, generación de gráficas, manipulación de datos y simulación de información. En este caso se utilizaron las librerías Flet para interfaces, Matplotlib para gráficas y Random para generación de datos.

###  Ejemplo (Gráficas con librerías)

```python
import matplotlib.pyplot as plt
import random

def generar_grafica_barras():
    productos = ["A", "B", "C", "D"]
    ventas = [15, 30, 45, 10]
    fig, ax = plt.subplots()
    ax.bar(productos, ventas)
    return fig

def generar_grafica_lineas():
    meses = ["Ene", "Feb", "Mar", "Abr", "May"]
    rendimiento = [10, 25, 18, 40, 35]
    fig, ax = plt.subplots()
    ax.plot(meses, rendimiento)
    return fig

def generar_grafica_dispersion():
    x = [i for i in range(20)]
    y = [random.randint(10, 50) for _ in range(20)]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    return fig
```

Este código permite generar diferentes tipos de gráficas utilizando librerías externas.

###  Imagen

<img width="1916" height="1017" alt="image" src="https://github.com/user-attachments/assets/1b9be295-bda4-4899-b801-1499453b0390" />


---

##  2.3 CREACIÓN DE COMPONENTES (VISUALES Y NO VISUALES)

###  Explicación

Los componentes pueden ser creados por el usuario para reutilizar código y facilitar la construcción de aplicaciones. Existen dos tipos principales: componentes visuales, que forman parte de la interfaz gráfica, y componentes no visuales, que contienen lógica del sistema.

###  Ejemplo 1 (Componente visual personalizado)

```python
import flet as ft

class TarjetaProducto(ft.Container):
    def __init__(self, nombre, descripcion, precio, imagen):
        super().__init__()
        self.width = 250
        self.padding = 10
        self.content = ft.Column(
            controls=[
                ft.Text(nombre),
                ft.Text(descripcion),
                ft.Text(f"$ {precio}")
            ]
        )
```

###  Ejemplo 2 (Uso del componente)

```python
tarjeta = TarjetaProducto(
    "Laptop Gamer",
    "Procesador i7 y 16GB RAM",
    25000,
    "laptop.jpg"
)
```

###  Ejemplo 3 (Componente con interacción)

```python
class TarjetaPerfil(ft.Container):
    def __init__(self, nombre, rol):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(nombre),
                ft.Text(rol),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ]
        )

    def saludar(self, e):
        print("Interacción con usuario")
```

###  Ejemplo 4 (Uso completo en aplicación)

```python
import flet as ft

productos = [
    {"nombre": "Laptop Gamer", "precio": 25000},
    {"nombre": "Smartphone", "precio": 12000}
]

def main(page: ft.Page):
    tarjetas = []
    for p in productos:
        tarjetas.append(
            TarjetaProducto(p["nombre"], "", p["precio"], "")
        )
    page.add(ft.Column(tarjetas))

ft.app(target=main)
```

###  Imagen

<img width="1571" height="889" alt="image" src="https://github.com/user-attachments/assets/45c2d33e-49eb-4d41-a3df-2340c51e0ac8" />


---

##  2.4 CREACIÓN Y USO DE PAQUETES / LIBRERÍAS DEFINIDAS POR EL USUARIO

###  Explicación

Para mantener el código organizado, es recomendable dividirlo en varios archivos o módulos. Esto permite reutilizar código, mejorar la estructura del programa y facilitar su mantenimiento.

###  Ejemplo (Uso de módulos)

Archivo principal:

```python
from tarjeta_producto import TarjetaProducto
```

Archivo secundario:

```python
class TarjetaProducto(ft.Container):
    pass
```

###  Ejemplo (Uso de DataClass)

```python
from dataclasses import dataclass

@dataclass
class PerfilUsuario:
    nombre: str
    rol: str
```

Este enfoque permite manejar los datos de forma clara y estructurada.

### 🖼️ Imagen

<img width="1038" height="469" alt="image" src="https://github.com/user-attachments/assets/b688ce4a-d504-4dc3-9935-fd01a4a5921b" />


---


##  CONCLUSIÓN

Los componentes y librerías son herramientas fundamentales en el desarrollo de software moderno. Permiten crear aplicaciones más rápidas, organizadas y reutilizables. Su correcta implementación mejora la calidad del código, reduce errores y facilita el desarrollo de proyectos complejos.

---

## BIBLIOGRAFÍA (APA)

Python Software Foundation. (2023). Python Documentation. https://docs.python.org
Matplotlib Developers. (2023). Matplotlib Documentation. https://matplotlib.org
Flet Team. (2024). Flet Documentation. https://flet.dev
Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1995). Design Patterns. Addison-Wesley

---
