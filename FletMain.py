import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera aplicacion con FLET"

    def obtener_valores(e):
        minutos = minutos_tf.value
        horas = horas_tf.value
        dia = dia_tf.value
        mes = mes_tf.value
        print(f"Los Minutos: {minutos}, Hora: {horas}, Dia: {dia}, Mes: {mes}")

    container = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_500,
        width=page.width,
        height=page.height,
    )
    minutos_tf = ft.TextField(label="Minutos")
    horas_tf = ft.TextField(label="Horas")
    dia_tf = ft.TextField(label="Dia")
    mes_tf = ft.TextField(label="Mes")
    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("PROGRAMADOR DE TAREAS"),
            minutos_tf,
            horas_tf,
            dia_tf,
            mes_tf,
            ft.ElevatedButton("Crear Tarea", on_click=obtener_valores),
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