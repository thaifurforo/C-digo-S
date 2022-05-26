import unittest
from calculadora import multiplicar, dividir

class TestCalculadora(unittest.TestCase):
  
  def test_multiplicar(self):
    # Dado / Given
    a = 1
    b = 2
    # Quando / Then
    resultado = multiplicar(a, b)
    
    # Então / When
    self.assertTrue(resultado == 2)
    
  def test_dividir_error(self):
    a = 2
    b = 0
    
    with self.assertRaises(ZeroDivisionError):
      dividir(a, b)
    
  