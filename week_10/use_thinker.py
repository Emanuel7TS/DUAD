import tkinter as tk
from tkinter import messagebox

# Crear una ventana oculta (no se muestra)
root = tk.Tk()
root.withdraw()

# Mostrar un mensaje
messagebox.showinfo("Información", "Este es un mensaje de información.")

import tkinter as tk
from tkinter.simpledialog import askstring

# Crear una ventana oculta
root = tk.Tk()
root.withdraw()

# Pedir entrada
respuesta = askstring("Entrada", "¿Cómo te llamas?")
print(f"Hola, {respuesta}!")

import tkinter as tk
from tkinter import messagebox

# Crear una ventana oculta
root = tk.Tk()
root.withdraw()

# Mostrar un cuadro de confirmación
respuesta = messagebox.askyesno("Confirmación", "¿Seguro que quieres continuar?")
if respuesta:
    print("Continuando con la acción.")
else:
    print("Acción cancelada.")

    import tkinter as tk
from tkinter import messagebox

# Crear una ventana oculta
root = tk.Tk()
root.withdraw()

# Mostrar un mensaje de error
messagebox.showerror("Error", "Algo salió mal.")

"""
Usamos tkinter para crear ventanas de mensajes, entradas y confirmaciones.
messagebox.showinfo() se usa para mostrar mensajes de información.
askstring() se usa para pedir una entrada de texto.
messagebox.askyesno() es útil para pedir una confirmación con "Sí" o "No".
messagebox.showerror() muestra un mensaje de error.
"""