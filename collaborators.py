import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Créditos")

label1 = tk.Label(root, text="- CALCULADORA -\n")
label1.pack(pady=1)

label2 = tk.Label(root, text="Santiago Emiliano Cheluja Martín\nLuis Alexis Martínez Rodríguez\nDiego Hernández Tadeo\n")
label2.pack(pady=1)

close_button = tk.Button(root, text="Cerrar", command=close_window)
close_button.pack()

root.mainloop()