import flet as ft

def IndexView(page:ft.Page, params):
    def CreateAppBar():
        app_bar = ft.AppBar(
            leading=ft.Image("images/csc_logo_100.png"),
            leading_width=40,
            title=ft.Text("Flet Template"),
            #center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.IconButton(ft.Icons.RESTART_ALT, on_click=restart_clicked),
                ft.IconButton(ft.Icons.FILTER_3),

            ],
        )
        return app_bar

    def restart_clicked(e):
         dlg = ft.AlertDialog(title=ft.Text("You clicked restart"))
         page.open(dlg)
    def btn_question1_clicked(e):
        page.go("/question/1")

    def btn_question2_clicked(e):
        page.go("/question/2")

    def btn_simple_clicked(e):
        page.go("/simple_view")

    appbar = CreateAppBar()
    question_data = {"question" : "Name five largest countries",
                "answer" : ["Russia", "China", "USA", "Canada", "Brazil"]}
    question_tb=ft.Text(value=question_data["question"], size=24)
    answer_column=ft.Column()
    i=1
    for answer in question_data["answer"]:
        number=ft.Text(value=i)
        a = ft.Text(value=answer)
        row=ft.Row(controls=[number,a])
        answer_column.controls.append(row)
        i+=1

    page.views.append(ft.View(
        "/",
        [appbar, question_tb, answer_column],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

    )
    )
    page.update()
