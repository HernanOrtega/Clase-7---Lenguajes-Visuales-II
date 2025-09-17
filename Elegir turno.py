# Ejercicio 2 - Elegir turno mañana/tarde/noche
import tkinter as tk
from tkinter import messagebox

def enviar_turno():
    turno_seleccionado = turno.get()
    if turno_seleccionado == "":
        messagebox.showerror("Error","Debes seleccionar un turno")
    else:
        messagebox.showinfo("Turno elegido",f"Has seleccionado el turno: {turno_seleccionado}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar turno")
ventana.geometry("300x200")

# Etiqueta
tk.Label(ventana, text="Elige un turno:", font=("Arial", 12)).pack(pady=10)

# Variable para guardar el turno
turno = tk.StringVar(value="") # valor inicial vacío

# Radiobutton
tk.Radiobutton(ventana, text="Mañana", variable=turno, value="Mañana").pack(anchor="w",padx=40)
tk.Radiobutton(ventana, text="Tarde", variable=turno, value="Tarde").pack(anchor="w",padx=40)
tk.Radiobutton(ventana, text="Noche", variable=turno, value="Noche").pack(anchor="w",padx=40)

# Botón enviar
btn_enviar = tk.Button(ventana, text="Enviar", command=enviar_turno)
btn_enviar.pack(pady=15)

ventana.mainloop()