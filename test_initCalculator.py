'''
DISCLAIMER
En la parte de pruebas aparecen que todas son erróneas (desconocemos por qué), pero haciendo la comprobación en la calculadora
todos los resultados son ciertos (a excepción de la última prueba, fue hecha a propósito para que se ejecutara el message box de error
y se mostraran las ventanas de los resultados)'''

import unittest
import math

from classicCalculator import ForTesting

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Inicialización de la calculadora
        self.calculator = ForTesting()

    def test_addition(self):
        result = self.calculator.evaluate_expression_with_base("2+2")
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = self.calculator.evaluate_expression_with_base("5-3")
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.evaluate_expression_with_base("2*3")
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calculator.evaluate_expression_with_base("6/2")
        self.assertEqual(result, 3)

    def test_multiple(self):
        result = self.calculator.evaluate_expression_with_base("(3+5)*10")
        self.assertEqual(result, 80)

    def test_sqrt(self):
        result = self.calculator.evaluate_expression_with_base("math.sqrt(16)")
        self.assertEqual(result, 4)

    def test_sin(self):
        result = self.calculator.evaluate_expression_with_base("math.sin(0)")
        self.assertEqual(result, 0)

    def test_cos(self):
        result = self.calculator.evaluate_expression_with_base("math.cos(0)")
        self.assertEqual(result, 1)

    def test_tan(self):
        result = self.calculator.evaluate_expression_with_base("math.tan(0)")
        self.assertEqual(result, 0)

    def test_log2(self):
        result = self.calculator.evaluate_expression_with_base("math.log2(8)")
        self.assertEqual(result, 3)

    def test_pi(self):
        result = self.calculator.evaluate_expression_with_base("1+")
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()