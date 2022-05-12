class NumberError(Exception):
  
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
    
def adicao(a: int, b: int) -> int:
  if (a < 0) or (b < 0):
    raise NumberError('Valor negativo')
  
  return a + b

try:
  resultado = adicao(1, 1)
  print(resultado)
  
  resultado = adicao(1, -1)
  print(resultado)
except Exception as ex:
  print(ex.args[0])
  
