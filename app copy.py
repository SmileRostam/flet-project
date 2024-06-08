import flet as ft

def main(page: ft.Page):
    page.title = "برنامه جوک"
    page.window_height = 700
    page.window_width = 400


    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    



    def btn_click(event):

# -------------- save user and pass valsues ----------------
        password_value = password_input.value
        username_value = username_input.value


# --------  ------ user and pass error -----------------
        if not username_input.value :
            username_input.error_text = "لطفا نام کاربری را وارد کنید"
            page.update()
        
        if not password_input.value :
            password_input.error_text = "لطفا رمز را وارد کنید"
            page.update()
        

        if username_input.value and password_input.value :

# ------------------------ show jokes page 1 -------------------
            txt_joke1 = ft.AlertDialog(title=ft.Text("1"))
            txt_joke2 = ft.AlertDialog(title=ft.Text("2"))
            txt_joke3 = ft.AlertDialog(title=ft.Text("3"))
            txt_joke4 = ft.AlertDialog(title=ft.Text("4"))
            txt_joke5 = ft.AlertDialog(title=ft.Text("5"))
            txt_joke6 = ft.AlertDialog(title=ft.Text("6"))
            txt_joke7 = ft.AlertDialog(title=ft.Text("7"))
            txt_joke8 = ft.AlertDialog(title=ft.Text("8"))
            txt_joke9 = ft.AlertDialog(title=ft.Text("9"))
            txt_joke10 = ft.AlertDialog(title=ft.Text("10"))
            txt_joke11 = ft.AlertDialog(title=ft.Text("11"))
            txt_joke12 = ft.AlertDialog(title=ft.Text("12"))

# ------------------------ show jokes page 2 -------------------

            txt_joke13 = ft.AlertDialog(title=ft.Text("13"))
            txt_joke14 = ft.AlertDialog(title=ft.Text("14"))
            txt_joke15 = ft.AlertDialog(title=ft.Text("15"))
            txt_joke16 = ft.AlertDialog(title=ft.Text("16"))
            txt_joke17 = ft.AlertDialog(title=ft.Text("17"))
            txt_joke18 = ft.AlertDialog(title=ft.Text("18"))
            txt_joke19 = ft.AlertDialog(title=ft.Text("19"))
            txt_joke20 = ft.AlertDialog(title=ft.Text("20"))
            txt_joke21 = ft.AlertDialog(title=ft.Text("21"))
            txt_joke22 = ft.AlertDialog(title=ft.Text("22"))
            txt_joke23 = ft.AlertDialog(title=ft.Text("23"))
            txt_joke24 = ft.AlertDialog(title=ft.Text("24"))

# ------------------------ show jokes page 3 -------------------

            txt_joke25 = ft.AlertDialog(title=ft.Text("25"))
            txt_joke26 = ft.AlertDialog(title=ft.Text("26"))
            txt_joke27 = ft.AlertDialog(title=ft.Text("27"))
            txt_joke28 = ft.AlertDialog(title=ft.Text("28"))
            txt_joke29 = ft.AlertDialog(title=ft.Text("29"))
            txt_joke30 = ft.AlertDialog(title=ft.Text("30"))
            txt_joke31 = ft.AlertDialog(title=ft.Text("31"))
            txt_joke32 = ft.AlertDialog(title=ft.Text("32"))
            txt_joke33 = ft.AlertDialog(title=ft.Text("33"))
            txt_joke34 = ft.AlertDialog(title=ft.Text("34"))
            txt_joke35 = ft.AlertDialog(title=ft.Text("35"))
            txt_joke36 = ft.AlertDialog(title=ft.Text("36"))
            
 #  ---------------  button call page 1  ---------------
            def joke1_click(e):
                page.dialog = txt_joke1
                txt_joke1.open = True
                page.update()
            def joke2_click(e):
                page.dialog = txt_joke2
                txt_joke2.open = True
                page.update()
            def joke3_click(e):
                page.dialog = txt_joke3
                txt_joke3.open = True
                page.update()
            def joke4_click(e):
                page.dialog = txt_joke4
                txt_joke4.open = True
                page.update()
            def joke5_click(e):
                page.dialog = txt_joke5
                txt_joke5.open = True
                page.update()
            def joke6_click(e):
                page.dialog = txt_joke6
                txt_joke6.open = True
                page.update()
            def joke7_click(e):
                page.dialog = txt_joke7
                txt_joke7.open = True
                page.update()
            def joke8_click(e):
                page.dialog = txt_joke8
                txt_joke8.open = True
                page.update()
            def joke9_click(e):
                page.dialog = txt_joke9
                txt_joke9.open = True
                page.update()
            def joke10_click(e):
                page.dialog = txt_joke10
                txt_joke10.open = True
                page.update()
            def joke11_click(e):
                page.dialog = txt_joke11
                txt_joke11.open = True
                page.update()
            def joke12_click(e):
                page.dialog = txt_joke12
                txt_joke12.open = True
                page.update()
# ---------------  page 2  -----------------
            def joke13_click(e):
                page.dialog = txt_joke13
                txt_joke13.open = True
                page.update()
            def joke14_click(e):
                page.dialog = txt_joke14
                txt_joke14.open = True
                page.update()
            def joke15_click(e):
                page.dialog = txt_joke15
                txt_joke15.open = True
                page.update()
            def joke16_click(e):
                page.dialog = txt_joke16
                txt_joke16.open = True
                page.update()
            def joke17_click(e):
                page.dialog = txt_joke17
                txt_joke12.open = True
                page.update()
            def joke18_click(e):
                page.dialog = txt_joke18
                txt_joke18.open = True
                page.update()
            def joke19_click(e):
                page.dialog = txt_joke19
                txt_joke19.open = True
                page.update()
            def joke20_click(e):
                page.dialog = txt_joke20
                txt_joke20.open = True
                page.update()
            def joke21_click(e):
                page.dialog = txt_joke21
                txt_joke21.open = True
                page.update()
            def joke22_click(e):
                page.dialog = txt_joke22
                txt_joke22.open = True
                page.update()
            def joke23_click(e):
                page.dialog = txt_joke23
                txt_joke23.open = True
                page.update()
            def joke24_click(e):
                page.dialog = txt_joke24
                txt_joke24.open = True
                page.update()
# ----------------  page 3  -------------------
            def joke25_click(e):
                page.dialog = txt_joke25
                txt_joke25.open = True
                page.update()
            def joke26_click(e):
                page.dialog = txt_joke26
                txt_joke26.open = True
                page.update()
            def joke27_click(e):
                page.dialog = txt_joke27
                txt_joke27.open = True
                page.update()
            def joke28_click(e):
                page.dialog = txt_joke28
                txt_joke28.open = True
                page.update()
            def joke29_click(e):
                page.dialog = txt_joke29
                txt_joke29.open = True
                page.update()
            def joke30_click(e):
                page.dialog = txt_joke30
                txt_joke30.open = True
                page.update()
            def joke31_click(e):
                page.dialog = txt_joke31
                txt_joke31.open = True
                page.update()
            def joke32_click(e):
                page.dialog = txt_joke32
                txt_joke32.open = True
                page.update()
            def joke33_click(e):
                page.dialog = txt_joke33
                txt_joke33.open = True
                page.update()
            def joke34_click(e):
                page.dialog = txt_joke34
                txt_joke34.open = True
                page.update()
            def joke35_click(e):
                page.dialog = txt_joke35
                txt_joke35.open = True
                page.update()
            def joke36_click(e):
                page.dialog = txt_joke36
                txt_joke36.open = True
                page.update()
            
            
            


# ----------------  page click --------------------- 
            def minus_click(e):
                if 1 < int(pageNumber.value) :
                    pageNumber.value = str(int(pageNumber.value) - 1)
                page.update()

            def plus_click(e):   
                if int(pageNumber.value) < 3 :
                    pageNumber.value = str(int(pageNumber.value) + 1)
                page.update()
# ---------------------- jokes --------------------
            joke1 = ft.ElevatedButton("joke1",on_click=joke1_click)
            joke2 = ft.ElevatedButton("joke2",on_click=joke2_click)
            joke3 = ft.ElevatedButton("joke3",on_click=joke3_click)
            joke4 = ft.ElevatedButton("joke4",on_click=joke4_click)
            joke5 = ft.ElevatedButton("joke5",on_click=joke5_click)
            joke6 = ft.ElevatedButton("joke6",on_click=joke6_click)
            joke7 = ft.ElevatedButton("joke7",on_click=joke7_click)
            joke8 = ft.ElevatedButton("joke8",on_click=joke8_click)
            joke9 = ft.ElevatedButton("joke9",on_click=joke9_click)
            joke10 = ft.ElevatedButton("joke10",on_click=joke10_click)
            joke11 = ft.ElevatedButton("joke11",on_click=joke11_click)
            joke12 = ft.ElevatedButton("joke12",on_click=joke12_click)

            joke13 = ft.ElevatedButton("joke13",on_click=joke13_click)
            joke14 = ft.ElevatedButton("joke14",on_click=joke14_click)
            joke15 = ft.ElevatedButton("joke15",on_click=joke15_click)
            joke16 = ft.ElevatedButton("joke16",on_click=joke16_click)
            joke17 = ft.ElevatedButton("joke17",on_click=joke17_click)
            joke18 = ft.ElevatedButton("joke18",on_click=joke18_click)
            joke19 = ft.ElevatedButton("joke19",on_click=joke19_click)
            joke20 = ft.ElevatedButton("joke20",on_click=joke20_click)
            joke21 = ft.ElevatedButton("joke21",on_click=joke21_click)
            joke22 = ft.ElevatedButton("joke22",on_click=joke22_click)
            joke23 = ft.ElevatedButton("joke23",on_click=joke23_click)
            joke24 = ft.ElevatedButton("joke24",on_click=joke24_click)

            joke25 = ft.ElevatedButton("joke25",on_click=joke25_click)
            joke26 = ft.ElevatedButton("joke26",on_click=joke26_click)
            joke27 = ft.ElevatedButton("joke27",on_click=joke27_click)
            joke28 = ft.ElevatedButton("joke28",on_click=joke28_click)
            joke29 = ft.ElevatedButton("joke29",on_click=joke29_click)
            joke30 = ft.ElevatedButton("joke30",on_click=joke30_click)
            joke31 = ft.ElevatedButton("joke31",on_click=joke31_click)
            joke32 = ft.ElevatedButton("joke32",on_click=joke32_click)
            joke33 = ft.ElevatedButton("joke33",on_click=joke33_click)
            joke34 = ft.ElevatedButton("joke34",on_click=joke34_click)
            joke35 = ft.ElevatedButton("joke35",on_click=joke35_click)
            joke36 = ft.ElevatedButton("joke36",on_click=joke36_click)
            
# ---------------------- show page ----------------------
            analog = ft.Row(
                    [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),pageNumber,ft.IconButton(ft.icons.ADD, on_click=plus_click)]
                    ,alignment=ft.MainAxisAlignment.CENTER
                    )
            page1 = False
            page2 = False
            page3 = False
            

# --------------------- page 1 add ----------------------
            if int(pageNumber.value) == 1:
                print(1)
                page.clean()
                page.update()

                page.add(ft.Row([joke1,joke2,joke3],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke4,joke5,joke6],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke7,joke8,joke9],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke10,joke11,joke12],alignment=ft.MainAxisAlignment.CENTER))
                
                page.add(ft.Column([analog],alignment=ft.MainAxisAlignment.END))
                page.update()
# --------------------- page 2 add ----------------------
            if int(pageNumber.value) == 2 :
                page.clean()
                page.update()

                page.add(ft.Row([joke13,joke14,joke15],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke16,joke17,joke18],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke19,joke20,joke21],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke22,joke23,joke24],alignment=ft.MainAxisAlignment.CENTER))

                page.add(ft.Column([analog],alignment=ft.MainAxisAlignment.END))
                print(2)
                page.update()
# --------------------- page 3 add ----------------------
            if int(pageNumber.value) == 3 :
                page.clean()
                page.update()

                page.add(ft.Row([joke25,joke26,joke27],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke28,joke29,joke30],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke31,joke32,joke33],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke34,joke35,joke36],alignment=ft.MainAxisAlignment.CENTER))

                page.add(ft.Column([analog],alignment=ft.MainAxisAlignment.END))
                print(3)
                page.update()




    wellcome = ft.Row([ft.Text(value="به برنامه خودت خوش امدید", color="black")],alignment=ft.MainAxisAlignment.CENTER)
    
    info_signup = ft.Row([ft.Text(value="برای ثبت نام , نام کاربری و رمز عبور را وارد کنید",color="black")],alignment=ft.MainAxisAlignment.CENTER)
    
    username_input = ft.TextField(hint_text="نام کاربری",color='gray', width=300)
    username_inputt = ft.Row([username_input],alignment=ft.MainAxisAlignment.CENTER)
    password_input = ft.TextField(hint_text="رمز عبور",color='gray', width=300) 
    password_inputt = ft.Row([password_input],alignment=ft.MainAxisAlignment.CENTER)
    SignUpButton = ft.ElevatedButton("ثبت نام", on_click=btn_click)
    SignUpButtonn = ft.Row([SignUpButton],alignment=ft.MainAxisAlignment.CENTER)
    
    pageNumber = ft.TextField(value="1", text_align="right", width=200)



    page.add(wellcome,info_signup,username_inputt,password_inputt,SignUpButtonn)
    

    page.update()
    

ft.app(target=main)