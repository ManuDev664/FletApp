import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera aplicacion con FLET"
    container = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_500,
        width=page.width,
        height=page.height,
    )
    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("PROGRAMADOR DE TAREAS"),
            ft.TextField(label="Minutos"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Segundos"),
            ft.ElevatedButton(label="Crear Tarea")
        ]
    )
    fila = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[columna]
    )

    # fila.controls = [columna]
    container.content = fila
    page.add(container)

    # etiqueta = ft.Text("¡Hola, Flet!")
    # page.add(etiqueta)
    # page.add(ft.Text("Adios"))

ft.app(target=main)