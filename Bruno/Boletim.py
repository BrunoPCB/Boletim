# coding utf-8


# Função que imprime um cabeçalho
def cabecalho():
    print('---' * 8)
    print('Notas Do 1º Bimestre')
    print('---' * 8)


# Função que imprime na tela as notas e a média(média recebe certa cor dependendo da situação do aluno
def media_cor(med):
    if med >= 7:
        print(f'|   MÉDIA    |   \033[1;36m{media}\033[m   |')
        print('---' * 8)
        print('|  SITUAÇÃO: APROVADO  |')
        print('---' * 8)
    elif 5 < med < 7:
        print(f'|   MÉDIA    |   \033[1;33m{media}\033[m   |')
        print('---' * 8)
        print('|  SITUAÇÃO: RECUPERAÇÃO  |')
        print('---' * 8)
    else:
        print(f'|   MÉDIA    |   \033[1;31m{media}\033[m   |')
        print('---' * 8)
        print('|  SITUAÇÃO: REPROVADO  |')
        print('---' * 8)


cabecalho()

# Inputs, pede ao usuário a nota 1, e nota 2
nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')

# Verificação de tipo de dados e alteração dos mesmos para tipos aritiméticos
if not(nota1.isalpha() and nota2.isalpha()):
    nota1, nota2 = float(nota1), float(nota2)
elif nota1.isdigit() and nota2.isdigit():
    nota1, nota2 = int(nota1), int(nota2)

# Cálculo da média
media = (nota1 + nota2) / 2

cabecalho()
# Devolução do resultado
print(f'|   NOTA 1   |   {nota1}   |\n'
      f'|   NOTA 2   |   {nota2}   |')

media_cor(media)
