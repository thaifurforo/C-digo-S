import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):
  
  def __atribuir_valores(self, a, b):
    return somar(a, b)
  
  def test_somar_valores_inteiros(self):
    self.assertTrue(somar(1, 2) == 3)
    self.assertTrue(somar(2, 2) == 4)
    
    self.assertEqual(somar(-1, 2), 1)
    self.assertEqual(somar(-2, 2), 0)
    
    resultado = self.__atribuir_valores(3, 2)
    self.assertTrue(resultado == 5)
    
  def test_somar_pontos_flutuantes(self):
    self.assertTrue(somar(1.4, 2.6) == 4)
    self.assertEqual(somar(1, 2.2), 3.2)
    
  def test_somar_tipo_resultado(self):
    self.assertEqual(type(somar(1, 2.1)), float)
    self.assertEqual(type(somar(1, 2)), int)
    self.assertTrue(type(somar(1.4, 2.6)) == float)
