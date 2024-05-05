import tkinter as tk
import subprocess

def window_classicCalculator():
    subprocess.Popen(["python", "classicCalculator.py"])

def window_collaborators():
    subprocess.Popen(["python", "collaborators.py"])

root = tk.Tk()
root.title("Menú")

open_classicCalculator = tk.Button(root, text="Calculadora Clásica", command=window_classicCalculator)
open_classicCalculator.pack(pady=10)

open_binaryCalculator = tk.Button(root, text="Calculadora Binaria")
open_binaryCalculator.pack(pady=10)

open_collaborators = tk.Button(root, text="Créditos", command=window_collaborators)
open_collaborators.pack(pady=10)

root.mainloop()