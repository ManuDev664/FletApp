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
        controls=[
            ft.Text("Hola, Flet!"),
            ft.Text("Esto es otra etiqueta"),
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