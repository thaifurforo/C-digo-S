class MaiconError(Exception):
  pass

a = 1
b = 0

try:
    a / b
except ZeroDivisionError as ex:
    print(f'Erro: {ex.args[0]}. Tente novamente.')
except AttributeError as ex_at:
    print('Erro de atributo.')
else:
    print('Erro.')


dividendo = 1
divisor = 0

try:
    if divisor == 0:
        raise AttributeError

    dividendo / divisor

# Todas as classes dos erros herdam da classe BaseException, portanto pra criar um alias pra qualquer erro que for gerado, usa:
except BaseException as ex:
    # Pode ser usado qualquer classe mãe da classe do erro. Por exemplo: ArithmeticError é uma classe mãe da ZeroDivisionError.
    print(f'Erro. Tente novamente.')
    # Nesse caso o args no ex estará vazio, porque o erro não é da classe BaseException. Por isso não dá pra usar o ex.args, pois a tupla estará vazia.

try:
  if dividendo == 1:
    raise MaiconError
except Exception as ex_maicon:
  print(ex_maicon.args)

try:
    if divisor == 0:
        raise AttributeError

    dividendo / divisor

# Como foi definido que vai trazer AttributeError (raise) ao invés do ZeroDivisionError se houver esse erro, não chega nem a rodar o except abaixo.
except ZeroDivisionError as ex:
    print(f'Erro: {ex.args[0]}. Tente novamente.')

