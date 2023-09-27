import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pages.timer import TimerApp

class HomePage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"Bienvenido, {self.username}")

        # Obtiene las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2

        self.root.geometry(f"400x300+{x}+{y}")

        self.welcome_label = tk.Label(root, text=f"Bienvenido, {self.username}!")
        self.welcome_label.pack()

        # Iniciar el temporizador automáticamente al cargar la página de inicio
        self.start_timer()

    def start_timer(self):
        timer_root = tk.Toplevel(self.root)
        timer_app = TimerApp(timer_root, self.username)
        timer_root.protocol("WM_DELETE_WINDOW", self.on_timer_close)

    def on_timer_close(self):
        # Cerrar la aplicación al finalizar el temporizador
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root, "Usuario de prueba")
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
