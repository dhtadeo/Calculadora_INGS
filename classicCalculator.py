import tkinter as tk
import math

class CalculatorApp(tk.Tk): 
    # Inicializa la calculadora
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.entry = tk.Entry(self, width=40)
        self.entry.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
        self.create_buttons()
        self.create_calc_button()
        self.create_clear_button()

    def create_buttons(self):
        # Layout para los botones de la calculadora
        buttons_layout = [
            ['(', ')', 'pi', '/', 'x^2'],
            ['7', '8', '9', '*', 'x^n'],
            ['4', '5', '6', '-', 'sqrt'],
            ['1', '2', '3', '+', 'nrt'],
            ['', '0', '.',]
        ]
        for i, row in enumerate(buttons_layout, start=1):
            for j, text in enumerate(row):
                button = CalculatorButton(self, text, command=lambda t=text: self.handle_button_click(t))
                button.grid(row=i, column=j, padx=0, pady=0)

    def create_clear_button(self):
        # Crear funcionalidad única para el botón de limpiar
        clear_button = CalculatorButton(self, 'C', command=self.clear_entry)
        clear_button.grid(row=5, column=3, padx=5, pady=5)

    def create_calc_button(self):
        # Crear funcionalidad única para el botón de calcular
        calc_button = CalculatorButton(self, '=', command=self.evaluate_expression)
        calc_button.grid(row=5, column=4, padx=5, pady=5)

    def handle_button_click(self, text):
        # Asignar funcionalidades con un nombre más reconocido
        if text == 'x^2':
            self.entry.insert(tk.END, '**2')
        elif text == 'x^n':
            self.entry.insert(tk.END, '**')
        elif text == 'sqrt':
            self.entry.insert(tk.END, 'math.sqrt(')
        elif text == 'nrt':
            self.entry.insert(tk.END, '**(1/')
        else:
            self.entry.insert(tk.END, text)

    def evaluate_expression(self):
        # Evaluar la expresión
        try:
            expression = self.entry.get()
            expression = expression.replace("pi", str(math.pi))
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error: División por cero")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error: Argumento inválido")
        except OverflowError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error: Desbordamiento")
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

class CalculatorButton(tk.Button):
    # Crear botones de la calculadora
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, width=5, height=2, **kwargs)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()


