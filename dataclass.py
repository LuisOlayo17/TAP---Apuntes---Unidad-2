import flet as ft
from dataclasses import dataclass

# Data Class para almacenar los datos del perfil
@dataclass
class PerfilUsuario:
    nombre: str
    rol: str
    color_borde: str = ft.Colors.BLUE


# Definición del componente personalizado
class TarjetaPerfil(ft.Container):
    def __init__(self, perfil: PerfilUsuario):
        super().__init__()

        self.perfil = perfil

        self.content = ft.Column(
            controls=[
                ft.Text(perfil.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(perfil.rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )

        self.border = ft.border.all(2, perfil.color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    def saludar(self, e):
        print(f"Interactuando con el componente de {self.perfil.nombre}")


def main(page: ft.Page):
    page.title = "Unidad 2: Componentes Definidos por el Usuario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Crear objetos usando la dataclass
    perfil1 = PerfilUsuario("Ana Garcia", "Desarrolladora Senior", ft.Colors.GREEN)
    perfil2 = PerfilUsuario("Carlos Ruiz", "Arquitecto de Software")

    # Crear los componentes visuales usando esos datos
    usuario1 = TarjetaPerfil(perfil1)
    usuario2 = TarjetaPerfil(perfil2)

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row([usuario1, usuario2], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)