import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera aplicacion con FLET"
    container = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_500,
        width=page.width,
        height=page.height,
    )
    minutos_tf = ft.TextField(label="Minutos")
    horas_tf = ft.TextField(label="Horas")
    segundos_tf = ft.TextField(label="Segundos")
    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("PROGRAMADOR DE TAREAS"),
            minutos_tf,
            horas_tf,
            segundos_tf,
            ft.ElevatedButton("Crear Tarea")
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