import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()
    if dato:  # Verificar que el campo no esté vacío
        lista.insert(tk.END, dato)
        entry.delete(0, tk.END)  # Limpiar el campo de texto después de agregar
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")

# Etiqueta para el campo de texto
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto para ingresar datos
entry = tk.Entry(root)
entry.pack(pady=5)

# Botón para agregar datos
btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista = tk.Listbox(root)
lista.pack(pady=10)

# Botón para limpiar la lista
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Iniciar el loop principal de la aplicación
root.mainloop()