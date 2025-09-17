# Ejercicio 1 - Téminos y Condiciones
import tkinter as tk
from tkinter import messagebox

def enviar():
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showerror("Error","El campo no puede estar vacio")
        return
    if not acepta_terminos.get():
        messagebox.showerror("Error","Debes aceptar los términos y condiciones")
        return
    messagebox.showinfo("Éxito",f"Formulario enviado correctamente. \nBienvenido, {nombre} !")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("300x200")

# Etiqueta y campo de texto
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

# Casilla de aceptación de términos
acepta_terminos = tk.BooleanVar()
chk_terminos = tk.Checkbutton(ventana, text="Acepto los términos y condiciones", variable=acepta_terminos)
chk_terminos.pack(pady=5)

# Botón enviar
btn_enviar = tk.Button(ventana, text="Enviar", command=enviar)
btn_enviar.pack(pady=10)

ventana.mainloop()