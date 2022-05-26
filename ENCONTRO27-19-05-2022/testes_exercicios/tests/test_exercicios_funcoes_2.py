from pytest import fixture
from funcoes import reverso

class TesteReverso:

  def test_reverso(self, fix):
    # dados
    valor = [127, 123, 12141]
    resultado = []

    
    # quando
    for i in valor:
        resultado.append(reverso(i))
    
    # então
    assert resultado == [721, 321, 14121]
    
@fixture
def fix():
  print('teste')

def test_reverso(fix):
  valor = 127
  resultado = reverso(valor)
  assert resultado == 721
  
def test_reverso_list():
  # dados
  valor = [127, 123, 12141]
  resultado = []
  
  # quando
  for i in valor:
      resultado.append(reverso(i))
  
  # então
  assert resultado == [721, 321, 14121]