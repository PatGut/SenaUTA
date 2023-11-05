import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def create_window(app):
    
    for widget in app.winfo_children():
        widget.destroy()

    
    customtkinter.CTkLabel(master=app, text="SELECCIONAR MÓDULO", font=("century gothic", 40), justify="left").pack(anchor="nw", side="top", padx=(56, 0), pady=(41, 0))

    quizzes_frame = customtkinter.CTkFrame(master=app, fg_color="transparent")
    quizzes_frame.pack(pady=(21, 0), padx=(50, 0), anchor="nw")

    movies_img_data = Image.open("movies-quiz-bg.png")
    movies_img = customtkinter.CTkImage(light_image=movies_img_data, dark_image=movies_img_data, size=(234, 91))
    customtkinter.CTkLabel(master=quizzes_frame, text="", image=movies_img, corner_radius=8).grid(row=0, column=0, sticky="nw")

    sports_img_data = Image.open("sports-quiz-bg.png")
    sports_img = customtkinter.CTkImage(light_image=sports_img_data, dark_image=sports_img_data, size=(234, 91))
    customtkinter.CTkLabel(master=quizzes_frame, text="", image=sports_img, corner_radius=8).grid(row=1, column=0, sticky="nw", pady=(30, 0))

    geography_img_data = Image.open("geography-quiz-bg.png")
    geography_img = customtkinter.CTkImage(light_image=geography_img_data, dark_image=geography_img_data, size=(175, 210))
    customtkinter.CTkButton(master=quizzes_frame, text="", image=geography_img, corner_radius=0, fg_color="transparent", command=lambda: show_classes(app)).grid(row=0, column=1, rowspan=2, sticky="nw")

    
    customtkinter.CTkButton(master=app, text="Volver", font=("century gothic", 24), command=lambda: return_to_home(app)).pack(anchor="w", padx=20, pady=20)

def show_classes(app):
    
    for widget in app.winfo_children():
        widget.destroy()

    
    customtkinter.CTkLabel(master=app, text="SELECCIONAR CLASE", font=("century gothic", 40), justify="left").pack(anchor="nw", side="top", padx=(56, 0), pady=(41, 0))

    classes_frame = customtkinter.CTkFrame(master=app, fg_color="transparent")
    classes_frame.pack(pady=(21, 0), padx=(50, 0), anchor="nw")

    class_list = ["Clase 1", "Clase 2", "Clase 3", "Clase 4", "Clase 5"]
    for c in class_list:
        customtkinter.CTkButton(master=classes_frame, text=c, font=("century gothic", 24), command=lambda c=c: class_button_click(c)).pack(anchor="w", padx=50, pady=10)

    
    customtkinter.CTkButton(master=classes_frame, text="Volver", font=("century gothic", 24), command=lambda: return_to_home(app)).pack(anchor="w", padx=50, pady=10)

def class_button_click(class_name):
    
    print(f"Se hizo clic en la clase: {class_name}")

def return_to_home(app):
    
    for widget in app.winfo_children():
        widget.destroy()
    create_window(app)

def quit_app(app):
    app.quit()

app = customtkinter.CTk()
app.attributes('-fullscreen', True)
app.title("SeñaUTA Educa")
app.configure(fg_color="#428ecc")

logo = customtkinter.CTkImage(dark_image=Image.open("C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes/SeñaUta.png"), size=(400, 250))
logouta = customtkinter.CTkImage(dark_image=Image.open("C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes/SeñaUta.png"), size=(150, 100))

frame1 = customtkinter.CTkFrame(master=app, fg_color="transparent")
frame1.pack()
Botones = customtkinter.CTkFrame(master=app, fg_color="transparent")
Botones.pack(pady=10, padx=20, expand=True)
frame2 = customtkinter.CTkFrame(master=app, fg_color="transparent")
frame2.pack(pady=10, padx=20, fill="both")

label1 = customtkinter.CTkLabel(master=frame1, image=logo, text="")
label1.pack(pady=10, padx=10)

def on_button_click():
    create_window(app)

button1 = customtkinter.CTkButton(master=Botones, fg_color="#1c1c3b", hover_color="#ebae31", text="CLASES", font=("century gothic", 80), text_color="white", command=on_button_click)
button1.pack(fill="both")

button_space = customtkinter.CTkLabel(master=Botones, text="", fg_color="transparent")
button_space.pack(fill="both")

quit_button = customtkinter.CTkButton(master=Botones, fg_color="#1c1c3b", hover_color="#ebae31", text="SALIR", font=("century gothic", 80), text_color="white", command=lambda: quit_app(app))
quit_button.pack(fill="both")

def resize_buttons(event):
    button_width = event.width // 3
    button_height = event.height // 3
    button1.configure(width=button_width, height=button_height)
    quit_button.configure(width=button_width, height=button_height)

app.bind("<Configure>", resize_buttons)

label2 = customtkinter.CTkLabel(master=frame2, image=logouta, text="", justify="right")
label2.pack(padx=1, pady=1, side="right")

app.mainloop()
