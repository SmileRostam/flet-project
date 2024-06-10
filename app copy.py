import flet as ft

def main(page: ft.Page):
    page.title = 'جک ها شوهر عمه ای'
    page.window_height = 700
    page.window_width = 400
    
    page.bgcolor = 'white'
    


    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    



    def btn_click(event):
        

# -------------- save user and pass valsues ----------------

        # password_value = password_input.value
        # username_value = username_input.value


# --------  ------ user and pass error -----------------
        if not username_input.value :
            username_input.error_text = "لطفا نام کاربری را وارد کنید"
            page.update()
        
        if not password_input.value :
            password_input.error_text = "لطفا رمز را وارد کنید"
            page.update()
        

        if username_input.value and password_input.value :

# ------------------------ show jokes page 1 -------------------
            txt_joke1 = ft.AlertDialog(title=ft.Text("امان از دسته این مانکنای جلویه مغازه‌ها امروز دماغ یکیشونو گرفتم برگشت بهم گفت مرض داری؟ نگو صاحب مغازه بود!! 😐"))
            txt_joke2 = ft.AlertDialog(title=ft.Text("دوستم گلوش چرک کرده بود پرسید چیکار کنم؟   خواستم بگم آب نمک قرقره کن حواسم   نبود گفتم آب قند قرقره کن   بنده خدا یه هفتس کلا نمیتونه صحبت کنه   دکتر گفته مجرای تنفسیش شکرک بسته 😂😂"))
            txt_joke3 = ft.AlertDialog(title=ft.Text("میدونی تو پودر نارگیل چیه ؟نارگیل,تو پودر نشاسته چیه؟نشاسته,آفرین تو پودر بچه چیه?بچه!عا خب نیستش، من بچه میخواستم ولی تو پودرش نیست."))
            txt_joke4 = ft.AlertDialog(title=ft.Text("به خدا من داشتم تو مدرسه درسمو میخوندم که یهو ناظم بهم گفت که از فردا با ولیت بیا منم گفتم نمیشه با اما بیام؟هیچی دیگه اخراجم کرد!!"))
            txt_joke5 = ft.AlertDialog(title=ft.Text("داداش میدونی ماهی ها غذاشونو تو چی سرخ میکنن؟نه داداش، تو چی سرخ میکنن؟ داداش معلومه دیگه، توی آدم تابه"))
            txt_joke6 = ft.AlertDialog(title=ft.Text("انقد خونه موندیم اسم اتاق رو گذاشتیم خونه اسم پذیرایی رو گذاشتیم بیرون "))
            txt_joke7 = ft.AlertDialog(title=ft.Text("میدونی وقتی تلویزیونا باهم کار خصوصی دارن بهم چی میگن؟چی میگن؟میگن بدو بیا تی وی کارت دارم"))
            txt_joke8 = ft.AlertDialog(title=ft.Text("می‌دونی کدوم لبنیات بیشتر از همه خدمت می‌کنه؟ ماست، چون همیشه می‌گن «خدمت از ماست.»"))
            txt_joke9 = ft.AlertDialog(title=ft.Text("گیاه‌خوارها پارتی می‌گیرن ویگن می‌ذارن."))
            txt_joke10 = ft.AlertDialog(title=ft.Text("میدونید اگه ماکارونیا پرخوری کنن چی میشه؟نودل میکنن"))
            txt_joke11 = ft.AlertDialog(title=ft.Text("دو تا گوجه داشتن با هم می‌رفتن. یهو ماشین از رو یکیشون رد می‌شه اون یکی می‌گه: رُب جون پاشو بریم"))
            txt_joke12 = ft.AlertDialog(title=ft.Text("می‌دونین ماهی‌ها بعد از اینکه غذا می‌خورن چیکار می‌کنن؟ دستمال میارن سفره ماهی رو پاک می‌کنن."))

# ------------------------ show jokes page 2 -------------------

            txt_joke13 = ft.AlertDialog(title=ft.Text("یه کرمه داشته رد می‌شده میفته تو قابلمه ماکارونی، می‌گه: عه حموم چقد شلوغه!"))
            txt_joke14 = ft.AlertDialog(title=ft.Text("می‌دونین اگه حیوون‌های نادر بمیرن چی می‌شه؟ نادر بی‌حیوون می‌شه."))
            txt_joke15 = ft.AlertDialog(title=ft.Text("یه غوله می‌ره مشهد می‌شه مشغول."))
            txt_joke16 = ft.AlertDialog(title=ft.Text("یارو دنبال قوری می‌گشت.. این ور رو نگاه کرد نبود، اون ور رو نگاه کرد بود."))
            txt_joke17 = ft.AlertDialog(title=ft.Text("چرا میلیاردر و میلیونر داریم ولی هزارِر نداریم؟ اینجا هم در حق ما معمولیا اجحاف شده"))
            txt_joke18 = ft.AlertDialog(title=ft.Text("یارو میره خواستگاری، از دختره خوشش نمیاد، به بابای عروس میگه: ما میریم یه دور میزنیم، بر می‌گردیم!"))
            txt_joke19 = ft.AlertDialog(title=ft.Text("از طرف می‌پرسن می‌دونی آبشار چیه؟ میگه آره همون رود خونه دیواری رو میگی دیگه!"))
            txt_joke20 = ft.AlertDialog(title=ft.Text("یارو می‌ره کله‌پزی فروشنده بهش می‌گه: چشم بذارم؟ یارو می‌گه: تو این یه ذره مغازه کجا قایم شم آخه؟"))
            txt_joke21 = ft.AlertDialog(title=ft.Text("یه روز تو تیمارستان همه داشتن می‌پریدن بالا پایین، رییس تیمارستان ازشون می‌پرسه «چه مرگتونه؟» می‌گن «ما سیب زمینیم داریم سرخ می‌شیم» می‌ره می‌بینه یکی نشسته رو زمین.پیش خودش می‌گه این حتما خوب شده. ازش می‌پرسه «چرا نشستی؟» می‌گه «من چسبیدم کف ماهی‌تابه»"))
            txt_joke22 = ft.AlertDialog(title=ft.Text("یارو می‌ره مغازه می‌پرسه: آقا خیارشور دارین؟ یارو می‌گه: آره داریم. می‌گه: لطف می‌کنین خیارهای‌ منم بشورین؟"))
            txt_joke23 = ft.AlertDialog(title=ft.Text("روباهی به زاغی گفت: چه دمی، چه سری، عجب پایی! زاغ عصبانی شد و گفت: بی‌تربیت! خجالت بکش، اون موقع من کلاس اول بودم الان دیگه شوهر دارم!"))
            txt_joke24 = ft.AlertDialog(title=ft.Text("می‌دونین اگه فیل لباس آبی بپوشه باباش بهش چی می‌گه؟ می‌گه: وای چقدر بهت میاد. حلا اگه همون فیله لباس صورتی بپوشه باباش چی بهش می‌گه؟ می‌گه قبلی بیشتر بهت میومد. حالا اگه فیله لباس قهوه‌ای بپوشه باباش بهش چی می‌گه؟ می‌گه: بسه چقدر لباس عوض می‌کنی!"))

# ------------------------ show jokes page 3 -------------------

            txt_joke25 = ft.AlertDialog(title=ft.Text("یه فیله می‌ره بالای درخت. یارو بهش می‌گه: آهای فیله اون بالا چی کار می‌کنی؟ می‌گه: من فیل نیستم گیلاسم. یارو می‌گه: نه تو فیلی گیلاس نیستی! فیله هم گوشاش رو تکون می‌ده می‌گه: ببین اینم برگامه!"))
            txt_joke26 = ft.AlertDialog(title=ft.Text("میدونید چرا الکترون ها سوار چرخ و فلک نمیشن؟چون باردارن براشون خوب نیست."))
            txt_joke27 = ft.AlertDialog(title=ft.Text("میدونی اسم دیگه وزیر نیرو چیه؟وزیر جرم ضرب در شتاب."))
            txt_joke28 = ft.AlertDialog(title=ft.Text("می دونید اون کدوم شهره که دوبار خداحافظی می کنه؟دوبای."))
            txt_joke29 = ft.AlertDialog(title=ft.Text("می دونید اگه ماهواره ها زیاد آب بخورن چی میشه؟دیششون می گیره."))
            txt_joke30 = ft.AlertDialog(title=ft.Text("می دونی به چیزی که دو تا ج داشته باشه چی می گن؟دوجداره."))
            txt_joke31 = ft.AlertDialog(title=ft.Text("می دونید تو کره به خر چی می گن؟کره خر."))
            txt_joke32 = ft.AlertDialog(title=ft.Text("می دونی تخم خر به کی می گن؟به کسی میگن که میره تخمه میخره."))
            txt_joke33 = ft.AlertDialog(title=ft.Text("می دونید وقتی یه سیب زمینی اعصابش از دست یکی خورد می شه چکار می کنه؟میزنه پورش می کنه."))
            txt_joke34 = ft.AlertDialog(title=ft.Text("می دونی لباس مورد علاقه دوچرخه ها چیه؟رکابی."))
            txt_joke35 = ft.AlertDialog(title=ft.Text("می دونی قابلمه ها وقتی گشنشون بشه چی میشه؟دلشون ظرف میره."))
            txt_joke36 = ft.AlertDialog(title=ft.Text("می دونی ساختمونی که جیش داره ولی به دستشویی نمی رسه چی میشه؟مصالحش درد می گیره."))
            
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

# -------------------------- light or dark ------------------------------
            








            

# ---------------------- show page ----------------------
            # pageNuber = ft.Row([ft.Text(value=1, color="black")],alignment=ft.MainAxisAlignment.CENTER)



            # analog = ft.Row(
            #         []
            #         ,alignment=ft.MainAxisAlignment.CENTER
                    # )
        
            
# --------------------- page 1 add ----------------------
            def page1_add():    
                print(1)
                page.clean()
                
                

                page.add(ft.Row([joke1,joke2,joke3],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke4,joke5,joke6],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke7,joke8,joke9],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke10,joke11,joke12],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke13,joke14,joke15],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke16,joke17,joke18],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke19,joke20,joke21],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke22,joke23,joke24],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke25,joke26,joke27],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke28,joke29,joke30],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke31,joke32,joke33],alignment=ft.MainAxisAlignment.CENTER))
                page.add(ft.Row([joke34,joke35,joke36],alignment=ft.MainAxisAlignment.CENTER))


                
                # page.add(ft.Row([backButton,nextButton],alignment=ft.MainAxisAlignment.CENTER))




                # page.add(ft.Column([analog],alignment=ft.MainAxisAlignment.END))
                page.update()

            page1_add()
# --------------------- page 2 add ----------------------
#             def page2_add():
#                 print(2) 
#                 page.clean()
#                 page.update()


#                 # page.add(ft.Column([analog],alignment=ft.MainAxisAlignment.END))
#                 page.update()
# # --------------------- page 3 add ----------------------
#             def page3_add():
#                 print(3)
#                 page.clean()
#                 page.update()


#                 # page.add(ft.Column([analog],alignment=ft.MainAxisAlignment.END))
#                 print(3)
#                 page.update()
            
#             page1 = True
    
            # def back_step ():
            #     if page3 == True :
            #         page3 = False
            #         page2 = True
            #         page2_add()
            #     elif page2 == True :
            #         page2 = False
            #         page1 = True
            #         page1_add()

            # def next_step ():
            #     if page1 == True:
            #         page1 = False
            #         page2_add()
            #         page2 = True
            #     elif page2 == True:
            #         page2 = False
            #         page3_add()
            #         page3 = True




            # backButton = ft.ElevatedButton(content=ft.Text("Next", color=ft.cupertino_colors.DESTRUCTIVE_RED),on_click=back_step)
                
            # nextButton = ft.ElevatedButton(content=ft.Text("Back", color=ft.cupertino_colors.DESTRUCTIVE_RED),on_click=next_step)

            
            




    # page1 = False
    # page2 = False
    # page3 = False
          


    wellcome = ft.Row([ft.Text(value="به برنامه خودت خوش امدید", color="black")],alignment=ft.MainAxisAlignment.CENTER)
    
    info_signup = ft.Row([ft.Text(value="برای ثبت نام , نام کاربری و رمز عبور را وارد کنید",color="black")],alignment=ft.MainAxisAlignment.CENTER)
    
    username_input = ft.TextField(hint_text="نام کاربری",color='gray', width=300, text_align="center")
    username_inputt = ft.Row([username_input],alignment=ft.MainAxisAlignment.CENTER)
    password_input = ft.TextField(hint_text="رمز عبور",color='gray', width=300, text_align="center") 
    password_inputt = ft.Row([password_input],alignment=ft.MainAxisAlignment.CENTER)
    SignUpButton = ft.ElevatedButton("ثبت نام", on_click=btn_click)
    SignUpButtonn = ft.Row([SignUpButton],alignment=ft.MainAxisAlignment.CENTER)
    
    

    page.add(ft.Column([wellcome,info_signup,username_inputt,password_inputt,SignUpButtonn],alignment=ft.MainAxisAlignment.CENTER))
    

    page.update()
    

ft.app(target=main)