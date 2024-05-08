import tkinter as tk

# Al presionar botón de cerrar
def close_window():
    root.destroy()

# Crear ventana
root = tk.Tk()
root.resizable(False, False)
root.geometry('300x150')
root.title("Créditos")

# Label 1
label1 = tk.Label(root, text="- CALCULADORA -\n")
label1.pack(pady=1)

# Label 2
label2 = tk.Label(root, text="Santiago Emiliano Cheluja Martín\nLuis Alexis Martínez Rodríguez\nDiego Hernández Tadeo\n\n")
label2.pack(pady=1)

# Botón de cerrar
close_button = tk.Button(root, text="Cerrar", command=close_window)
close_button.pack()

# Iniciar ventana
root.mainloop()