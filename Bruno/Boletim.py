# Função que imprime um cabeçalho
def cabecalho(bim):
    print('---' * 8)
    print(f'Notas do {bim}º Bimestre')
    print('---' * 8)


# Função que imprime na tela as notas e a média(média recebe certa cor dependendo da situação do aluno
def media_cor(med):
    if med >= 7:
        print(f'|   MÉDIA    |   {media:.2f}   |')
        print('---' * 8)
        print('|  SITUAÇÃO: APROVADO  |')
        print('---' * 8)
    elif 5 < med < 7:
        print(f'|   MÉDIA    |   {media:.2f}   |')
        print('---' * 8)
        print('|  SITUAÇÃO: RECUPERAÇÃO  |')
        print('---' * 8)
    else:
        print(f'|   MÉDIA    |   {media:.2f}   |')
        print('---' * 8)
        print('|  SITUAÇÃO: REPROVADO  |')
        print('---' * 8)

soma = 0

# Dicionário criado para armazenar as notas de forma mais fácil de encontrar
notas = {'nota 1': 0, 'nota 2': 0}

# Quantas notas ele deseja adicionar
qtd_notas = int(input('Quantas notas deseja adicionar: '))

# Verificação de quantidade de notas e adicina ao dicionário
for num in range(qtd_notas):
    nome_key = f'nota {num + 1}'
    value = 0
    notas[nome_key] = value

tamanho_notas = len(notas)
    
for v in range(4):
    cabecalho(v+1)
    
    # Loop para mostrar as notas.
    for va in notas:
        # Inputs, pede ao usuário nota1, nota2, ... notaN.
        notas[va] = input(f'Digite a {va}: ')

        # Substitui a vígula por ponto caso haja vírgula no valor.
        if ',' in notas[va]:
            notas[va] = notas[va].replace(',','.')
    
    for keys in notas:
        # Verificação de tipo de dados e alteração dos mesmos para tipos aritiméticos
        if not(notas[keys].isalpha()):
            notas[keys] = float(notas[keys])
        elif notas[keys] .isdigit():
            notas[keys]  = int(notas[keys] )

    for valor in notas:
        # Soma os valores
        soma += notas[valor]
        # Cálculo da média
        media = soma / tamanho_notas

        
    cabecalho(v+1)
    for chave, val in notas.items():
        # Devolução do resultado
        print(f'|   {chave}      |   {notas[chave]}   |')

    media_cor(media)
    print()

    # Alterações em variáveis
    v += 1
    soma = 0
