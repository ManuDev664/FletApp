import flet as ft
import datetime

from certifi import contents


def main(page: ft.Page):
    page.title = "Mi primera aplicacion con FLET"

    def abrir_dialog (mensaje):
        dialog.content = ft.Text(mensaje)
        dialog.open = True
        page.update()

    def cerrar_dialog(e):
        dialog.open = False
        page.update()

    def abrir_selector(e):
        fecha_dp.open = True
        page.update()

    def seleccionar_fecha(e):
        fecha_tx.value = f"{fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}"
        page.update()

    def obtener_valores(e):
        minutos = minutos_drop.value
        horas = horas_drop.value
        dia = fecha_dp.value.day
        mes = fecha_dp.value.month
        evento = evento_tf.value
        print(f"Dia: {dia}, Mes: {mes}, Hora: {horas}, Minutos: {minutos}, Evento: {evento}")

        if minutos is None:
            abrir_dialog("Debes seleccionar los minutos")
            return
        elif horas is None:
            abrir_dialog("Debes seleccionar las horas")
            return
        elif evento == "" or evento is None:
            abrir_dialog("Indica el evento")
            return
    def obtener_minutos():
        # Crear una lista vacia para almacenar las opciones
        lista_minutos = []

        for i in range(1,60):
            minutos_str = str(i).zfill(2)
            opcion = ft.dropdown.Option(text=minutos_str,
                                        key=minutos_str)
            lista_minutos.append(opcion)

        return lista_minutos

    def obtener_horas():
        lista_horas = []

        for i in range(0,24):
            horas_str = str(i).zfill(2)
            opcion = ft.dropdown.Option(text=horas_str,
                                        key=horas_str)
            lista_horas.append(opcion)

        return lista_horas

    container = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_500,
        width=page.width,
        height=page.height,
    )

    minutos_drop = ft.Dropdown(label="Minutos",
                               options=obtener_minutos(),
                               width=300,
                               max_menu_height=200)

    horas_drop = ft.Dropdown(label="Horas",
                             options=obtener_horas(),
                             width=300,
                             max_menu_height=200)
    dia_tf = ft.TextField(label="Dia")
    #mes_tf = ft.TextField(label="Mes"),
    evento_tf = ft.TextField(label="Evento")
    fecha_dp = ft.DatePicker(value=datetime.datetime.now(), on_change=seleccionar_fecha)
    fecha_tx = ft.Text(f"{fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}")
    boton_fecha = ft.ElevatedButton("Selecciona la fecha", on_click=lambda e: abrir_selector(e))

    dialog = ft.AlertDialog(modal=True, title=ft.Text("Información"), content=ft.Text("Test"),
                            actions=[ft.TextButton("Aceptar", on_click=cerrar_dialog)])

    columna=ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
                    ft.Text("PROGRAMADOR DE TAREAS"),
                    minutos_drop,
                    horas_drop,
                    fecha_tx,
                    boton_fecha,
                    evento_tf,
                    ft.ElevatedButton("Crear Tarea", on_click=obtener_valores),
        ]
    )
    fila=ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[columna]
    )

    # fila.controls = [columna]
    container.content = fila
    page.overlay.append(fecha_dp)
    page.overlay.append(dialog)
    page.add(container)

    # etiqueta = ft.Text("¡Hola, Flet!")
    # page.add(etiqueta)
    # page.add(ft.Text("Adios"))

ft.app(target=main, view=ft.WEB_BROWSER)