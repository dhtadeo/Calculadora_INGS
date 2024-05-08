import tkinter as tk
import subprocess

# Ejecutar classicCalculator
def window_classicCalculator():
    subprocess.Popen(["python", "classicCalculator.py"])

# Ejecutar collaborators
def window_collaborators():
    subprocess.Popen(["python", "collaborators.py"])

# Crear ventana
root = tk.Tk()
root.title("Menú")
root.resizable(False, False)
root.geometry('300x100')

# Botón de abrir calculadora
open_classicCalculator = tk.Button(root, text="Calculadora", command=window_classicCalculator)
open_classicCalculator.pack(pady=10)

# Botón de mostrar colaboradores
open_collaborators = tk.Button(root, text="Créditos", command=window_collaborators)
open_collaborators.pack(pady=10)

# Iniciar programa
root.mainloop()