import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pages.home import HomePage
import webbrowser

def login_user():
    def verify_login():
        username = username_entry.get()
        password = password_entry.get()

        if check_credentials(username, password):
            root.withdraw()  # Oculta la ventana de inicio de sesión
            open_home_page(username)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def check_credentials(username, password):
        with open("login/users.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and password == stored_password:
                    return True
        return False
    
    def open_home_page(username):
        home_root = tk.Tk()
        home_page = HomePage(home_root, username)
        home_root.mainloop()

    def open_web_page(event):
        webbrowser.open("https://tu-pagina-web.com")  # Reemplaza con tu URL

    root = tk.Tk()
    root.title("Inicio de Sesión")

    logo_image = Image.open("./img/logo.png")
    logo_photo = ImageTk.PhotoImage(logo_image)
    root.iconphoto(True, logo_photo)

    background_image = Image.open("./img/background.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    window_width = 800
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg="#000000")
    root.resizable(False, False)

    username_label = tk.Label(root, text="Nombre de Usuario:")
    username_label.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Contraseña:")
    password_label.pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Iniciar Sesión", command=verify_login)
    login_button.pack()

    # Agregar el mensaje de "copyright 2023" como un enlace a una página web
    copyright_label = tk.Label(root, text="Copyright 2023", fg="black", cursor="hand2")
    copyright_label.pack(side="bottom", anchor="se")
    copyright_label.bind("<Button-1>", open_web_page)

    root.mainloop()

if __name__ == "__main__":
    login_user()
