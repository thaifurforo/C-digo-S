"""
How bootcamps - Stone / código[s]
Data: 24/02/2022
Facilitador: Henrique Junqueira Branco
Tema: Estrutura condicional
"""

aluno = 'Thainara Lessa Furforo'

nota1 = float(input('Digite a primeira nota: '))

nota2 = float(input('Digite a segunda nota: '))

nota3 = float(input('Digite a terceira nota: '))

notas = [nota1, nota2, nota3]

nota_media = sum(notas) / len(notas)

nota_minima_aprovacao = 7
nota_minima_recuperacao = 6

if nota_media >= nota_minima_aprovacao:
    status = 'aprovado'
elif nota_media >= nota_minima_recuperacao:
    status = 'para recuperação'
else:
    status = 'reprovado'

nota_media_arred = round(nota_media, 2)

print(
    f'A média do aluno {aluno} é {nota_media_arred} e este aluno foi {status}.')


if (nota_media >= nota_minima_aprovacao) and (aluno == 'Thainara'):
    nota_media = 10
    status = 'aprovado'
elif nota_media >= nota_minima_recuperacao:
    status = 'para recuperação'
else:
    status = 'reprovado'

nota_media_arred = round(nota_media, 2)

print(
    f'\nA média do aluno {aluno} é {nota_media_arred} e este aluno foi {status}.')
# Ao ter sido utilizado == ao invés de in na condição, e tendo colocado tudo em apenas uma condição, como o nome do aluno não é apenas 'Thainara', qualquer nota acima da nota mínima para recuperação irá para recuperação, mesmo se for maior que a nota mínima para aprovação (primeira condição retornará False independente das notas informadas)


if nota_media >= nota_minima_aprovacao:
    status = 'aprovado'
    if 'Thainara' in aluno:
        nota_media = 10
elif nota_media >= nota_minima_recuperacao:
    status = 'para recuperação'
else:
    status = 'reprovado'

nota_media_arred = round(nota_media, 2)

print(
    f'\nA média do aluno {aluno} é {nota_media_arred} e este aluno foi {status}.')
# Nesse caso foi utilizado in para verificar se o nome 'Thainara' está no nome do aluno, o que retornará verdadeiro e substituirá a nota_media por 10. O if dentro de if garante que mesmo se o nome 'Thainara' não estiver dentro do aluno, irá funcionar a parte do status, pois independe do nome do aluno.

if (nota_media >= nota_minima_aprovacao) or (aluno in 'Thainara'):
    nota_media = 10
    status = 'aprovado'
elif nota_media >= nota_minima_recuperacao:
    status = 'para recuperação'
else:
    status = 'reprovado'

nota_media_arred = round(nota_media, 2)

print(
    f'\nA média do aluno {aluno} é {nota_media_arred} e este aluno foi {status}.')
# Se o aluno contiver 'Thainara', independente da nota_media anterior, a nota_media será alterada para 10 e o status será 'aprovado'.
# Ao mesmo tempo, mesmo se o aluno não contiver 'Thainara', mas a nota_media anterior for acima da nota_minima_aprovacao, a nota_media passa a ser 10 e o status será 'aprovado'.


if (nota_media >= nota_minima_aprovacao) and not (aluno in 'Thainara'):
    nota_media = 10
    status = 'aprovado'
elif nota_media >= nota_minima_recuperacao:
    status = 'para recuperação'
else:
    status = 'reprovado'

nota_media_arred = round(nota_media, 2)

print(
    f'\nA média do aluno {aluno} é {nota_media_arred} e este aluno foi {status}.')
# Se o aluno contiver 'Thainara', mesmo se a nota_media for acima da nota_minima_aprovacao, o aluno será enviado para recuperação (se nota_media >= nota_minima_recuperacao) ou reprovado (se nota_media < nota_minima_recuperacao)
# Ao mesmo tempo, mesmo se o aluno não contiver 'Thainara', mas a nota_media anterior for acima da nota_minima_aprovacao, a nota_media passa a ser 10 e o status será 'aprovado'.

if nota_media >= nota_minima_aprovacao:
    status = 'aprovado'

elif nota_media >= nota_minima_recuperacao:
    novas_notas = notas
    novas_notas.remove(min(novas_notas))
    nova_media = sum(novas_notas) / len(novas_notas)

    if nova_media >= nota_minima_aprovacao:
        nota_media = nova_media
        status = f'aprovado com len{novas_notas}'

    else:
        status = 'para recuperação'
else:
    status = 'reprovado'

nota_media_arred = round(nota_media, 2)

print(
    f'\nA média do aluno {aluno} é {nota_media_arred} e este aluno foi {status}.')
# Se a nota do aluno estiver dentro da faixa de recuperação (maior igual a 6 e menor que 7), é descartada a menor nota e verificado se dessa forma a média entra na faixa de aprovação.
# Em caso positivo, o status informado é que ele foi aprovado, mas com um número menor de notas.
# Já caso, descartando-se a nota, a média continue estando dentro da faixa de recuperação, será utilizada a média original, e não a média alterada (com a remoção da menor nota).
