# Ejercicio 3 - Selector de lenguajes de programación
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Selector de Lenguajes de Programación")

# Diccionario con lenguajes y sus descripciones
lenguajes = {
    "Python": "Lenguaje interpretado, fácil de leer y versátil. Ideal para principiantes y ciencia de datos.",
    "JavaScript": "Lenguaje de scripting para desarrollo web. Se ejecuta en el navegador y en el servidor (Node.js).",
    "Java": "Lenguaje orientado a objetos, robusto y multiplataforma. Usado en aplicaciones empresariales y Android.",
    "C#": "Lenguaje moderno de Microsoft, usado en desarrollo de juegos (Unity) y aplicaciones Windows.",
    "C++": "Lenguaje de alto rendimiento, usado en sistemas operativos, juegos y aplicaciones críticas.",
}

# Variable para almacenar la selección del Combobox
seleccion = tk.StringVar()

# Crear el Combobox
combobox = ttk.Combobox(root, textvariable=seleccion, state="readonly")
combobox['values'] = list(lenguajes.keys())  # Agregar los lenguajes como opciones
combobox.grid(pady=10, padx=10)

# Label para mostrar la descripción
descripcion_label = tk.Label(root, text="Selecciona un lenguaje para ver su descripción.", wraplength=300)
descripcion_label.grid(pady=10, padx=10)

# Función para actualizar la descripción al seleccionar un lenguaje
def actualizar_descripcion(event):
    lenguaje = seleccion.get()
    descripcion = lenguajes.get(lenguaje, "Selecciona un lenguaje válido.")
    descripcion_label.config(text=descripcion)

# Asociar la función al evento de selección del Combobox
combobox.bind("<<ComboboxSelected>>", actualizar_descripcion)

# Iniciar el loop de la aplicación
root.mainloop()