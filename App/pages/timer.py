# timer.py

import tkinter as tk
from tkinter import messagebox
from dist import var  # Importa la variable de tiempo desde var.py

class TimerApp:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"Temporizador para {self.username}")
        self.root.geometry("300x200")

        self.seconds_remaining = 10  # Establece la cantidad de segundos deseados

        self.timer_label = tk.Label(root, text=f"Tiempo restante: {self.seconds_remaining} segundos")
        self.timer_label.pack()

        self.update_timer()

    def update_timer(self):
        if self.seconds_remaining > 0:
            self.timer_label.config(text=f"Tiempo restante: {self.seconds_remaining} segundos")
            self.seconds_remaining -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.root.destroy()  # Cierra la ventana del temporizador al finalizar

if __name__ == "__main__":
    root = tk.Tk()
    # El segundo argumento (10) representa la duración de la sesión en segundos (puedes ajustarlo)
    app = TimerApp(root, "Usuario de prueba")
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
