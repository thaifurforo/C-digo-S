# language: pt

Funcionalidade: teste de cadastro de veículos

Cenário: validar o retorno do método inserir veículo
  Dado o veículo com identificação "123", placa "JTC1988" e quilometragem "123456"
  Quando efetuado o cadastro
  Então o resultado deve ser "Verdadeiro"

Cenário: validar o retorno do método consultar veículos
  Dado o veículo com identificação "45645", placa "teste" e quilometragem "456475"
  Quando efetuado o cadastro
  Então o veículo cadastrado deve ter os dados identificação "45645", placa "teste" e quilometragem "456475"

Cenário: validar a listagem de veículos cadastrados
  Dados os cadastros dos dados de veículos:
  | id | placa | km |
  | 1 | "jtc1988" | "1231" |
  | 2 | "abc1234" | "7456" |
  | 3 | "sad4789" | "5010" |
  | 4 | "pop7985" | "8014" |
  Quando listados todos os veículos
  Então o resultado deve ser:
  | id | placa | km |
  | 1 | "jtc1988" | "1231" |
  | 2 | "abc1234" | "7456" |
  | 3 | "sad4789" | "5010" |
  | 4 | "pop7985" | "8014" |