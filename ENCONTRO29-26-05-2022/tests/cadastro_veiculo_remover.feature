# language: pt

Funcionalidade: Testar a rotina de remoção de veículos de uma lista

Cenário: validar a remoção por id
  Dados os cadastros dos dados de veículos:
  | id | placa | km |
  | 1 | "jtc1988" | "1231" |
  | 2 | "abc1234" | "7456" |
  | 3 | "sad4789" | "5010" |
  | 4 | "pop7985" | "8014" |
  Quando o veículo com id "1" for removido
  Então a quantidade de veículos cadastrados deve ser 3