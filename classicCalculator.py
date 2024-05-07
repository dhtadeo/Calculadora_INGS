import tkinter as tk
from tkinter import messagebox
import math
from datetime import datetime

class CalculatorApp(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.entry = tk.Entry(self, width=45)
        self.entry.grid(row=0, column=0, columnspan=6, padx=1, pady=1)

        # Iniciar métodos
        self.create_buttons()
        self.create_calc_button()
        self.create_clear_button()
        self.create_history_button()
        self.create_binary_button()

        # Lista que agrupará el historial de operaciones
        self.history = []

        # Evitar que la ventana se pueda maximizar porque no quiero (se ve mal)
        self.resizable(False, False)

    def create_buttons(self):
        buttons_layout = [
            ['(', ')', 'π', '/', 'x^2', 'sin'],
            ['7', '8', '9', '*', 'x^n', 'cos'],
            ['4', '5', '6', '-', 'sqrt', 'tan'],
            ['1', '2', '3', '+', 'nrt', 'log2'],
            ['', '0', '.',]
        ]
        for i, row in enumerate(buttons_layout, start=1):
            for j, text in enumerate(row):
                button = CalculatorButton(self, text, command=lambda t=text: self.handle_button_click(t))
                button.grid(row=i, column=j, padx=0, pady=0)

    def create_clear_button(self):
        clear_button = CalculatorButton(self, 'CLR', command=self.clear_entry)
        clear_button.grid(row=5, column=4, padx=0, pady=0)

    def create_calc_button(self):
        calc_button = CalculatorButton(self, '=', command=self.evaluate_expression)
        calc_button.grid(row=5, column=3, padx=0, pady=0)

    def create_history_button(self):
        history_button = CalculatorButton(self, 'HIST', command=self.show_history)
        history_button.grid(row=5, column=5, padx=0, pady=0)

    def create_binary_button(self):
        binary_button = CalculatorButton(self, 'MORE', command=self.show_other_results)
        binary_button.grid(row=5, column=0, padx=0, pady=0)

    def handle_button_click(self, text):
        if text == 'x^2':
            self.entry.insert(tk.END, '**2')
        elif text == 'x^n':
            self.entry.insert(tk.END, '**')
        elif text == 'sqrt':
            self.entry.insert(tk.END, 'math.sqrt(')
        elif text == 'nrt':
            self.entry.insert(tk.END, '**(1/')
        elif text == 'sin':
            self.entry.insert(tk.END, 'math.sin(')
        elif text == 'cos':
            self.entry.insert(tk.END, 'math.cos(')
        elif text == 'tan':
            self.entry.insert(tk.END, 'math.tan(')
        elif text == 'log2':
            self.entry.insert(tk.END, 'math.log2(')
        else:
            self.entry.insert(tk.END, text)

    def handle_error(self, error):
        messagebox.showerror("Error", f"{type(error).__name__}\n{str(error)}")
        self.entry.delete(0, tk.END)

    def evaluate_expression(self):
        try:
            expression = self.entry.get()
            expression = expression.replace("π", str(math.pi))
            result = eval(expression)
            operation = {'operation': expression, 'result': result, 'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            self.history.append(operation)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.handle_error(e)
            

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("Historial de Operaciones")
        history_text = tk.Text(history_window, height=20, width=50)
        history_text.pack()
        for entry in self.history:
            history_text.insert(tk.END, f"> {entry['operation']}\n = {entry['result']}\nAt: {entry['time']}\n\n")
        history_text.config(state=tk.DISABLED)

    def show_other_results(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            to_bin = bin(result)[2:]
            to_oct = oct(result)[2:]
            to_hex = hex(result)[2:]
            messagebox.showinfo(f"Más resultados", f"> {expression}\n\nDEC: {result}\nBIN: {to_bin}\nOCT: {to_oct}\nHEX: {to_hex}")
        except Exception as e:
            self.handle_error(e)

class CalculatorButton(tk.Button):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, width=5, height=2, **kwargs)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()