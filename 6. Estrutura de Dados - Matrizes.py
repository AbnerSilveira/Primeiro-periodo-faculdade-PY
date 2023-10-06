# 1)exercicos base de Matrizes:
# a)Preencha pelo teclado uma matriz 3x 3 com números inteiros.

mat=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        mat[l][c]=int(input("um numero inteiro"))

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)        

# b) Imprima a matriz de números inteiros em formato matriz:

for l in range(3):
    for c in range(3):
        print (mat[l][c],"|", end='')
print()

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# c) Realize a soma de cada linha da matriz. Apresente o resultado:

somalinha = 0

for l in range(3):
    for c in range(3):
        somalinha = (somalinha + mat[l][c])
    print ("A soma da linha", l, "é:", somalinha)
    somalinha = 0

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# d) Realize a soma de cada coluna da matriz. Apresente o resultado:

somacoluna = 0
for c in range(3):
    for l in range(3):
        somacoluna = (somacoluna + mat[l][c])
    print ("A soma da coluna", c, "é:", somacoluna)
    somacoluna = 0

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# e)Realize a soma dos elementos da diagonal principal

somaDiagonal = 0

for l in range(3):
    for c in range(3):
        if (l == c):
            somaDiagonal = somaDiagonal + mat[l][c]
print("A soma dos elementos da diagonal principal é :", somaDiagonal)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# f) Gere a matriz transposta da matriz de número inteiros criada na letra “a”. Imprima a matriz transposta.
# Obs: Na transposta a linha vira coluna.

transposta = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(3):
    for c in range(3):
        transposta[l][c] = mat[c][l]
for l in range(3):
    for c in range(3):
        print (transposta[l][c],"|", end = '')
print()

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# g) Verifique e imprima quantos números são pares e quantos são impares.:

contpar = contaimpar = 0

for l in range(3):
    for c in range(3):
        if (mat[l][c]%2==0):
            contpar=contpar+1
        else:
            contimpar=contimpar+1
print("A quantidade de números pares é:", contpar)
print("A quantidade de números pares é:", contimpar)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# h) A soma de todos os elementos da matriz.

somaGeral = 0

for l in range(3):
    for c in range(3):
        somaGeral = (somaGeral + mat[l][c])
print ("A soma geral é:", somaGeral)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# i) Verifique e imprima o primeiro maior elemento da matriz e em que linha e coluna ele se encontra.

maior = 0
linhamaior = 0
colunamaior = 0

for l in range(3):
    for c in range(3):
        if (mat[l][c] > maior):
            maior = mat[l][c]
            linhamaior = l
            colunamaior = c
print ("O maior elemento é:", maior, "e encontrase na linha", linhamaior, " e na coluna ", colunamaior)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 2) Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', 10, 9], ['Brasil',
# 'Espanha', 5, 7], ['Italia', 'Espanha', 7,8]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na
# lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela: a)
# o total de faltas do campeonato b) o time que fez mais faltas c) o time que fez menos faltas

#criando a lista conforme o enunciado do exercício
lista_jogos = [['Brasil', 'Italia', 10, 9],
 ['Brasil', 'Espanha', 5, 7],
 ['Italia', 'Espanha', 7, 8]]
#inicializando as variáveis
total_faltas = 0
time_mais_faltas = ''
time_menos_faltas = ''
mais_faltas = 0
menos_faltas = 0
#Varendo a matriz e fazendo a soma das faltas
for jogo in lista_jogos:
    faltas_Brasil = lista_jogos[0][2]+lista_jogos[1][2]
    faltas_Italia = lista_jogos[0][3]+lista_jogos[2][2]
    faltas_Espanha= lista_jogos[1][3]+lista_jogos[2][3]

#jogando o resultado das somas das faltas de cada pais para uma outra matriz de faltas
lista_faltas = [["Brasil", "Itália", "Espanha"],[0,0,0]]
lista_faltas[1][0] = faltas_Brasil
lista_faltas[1][1] = faltas_Italia
lista_faltas[1][2] = faltas_Espanha

#imrprimindo a matriz de faltas
print ("Total de Faltas")
for l in range(2):
    for c in range (3):
        print (lista_faltas[l][c],"|", end='')
    print()
print()

#verificando quais países possuem mais e menos faltas
mais_faltas = max(lista_faltas[1])
menos_faltas = min(lista_faltas[1])

print ("Pais(es) com maior número de faltas:")
for c in range (3):
    if (lista_faltas[1][c]) == (mais_faltas):
        print ("Pais: ", lista_faltas[0][c], "- Número de faltas= ", lista_faltas[1][c])
print()

print ("Pais(es) com menor número de faltas")
for c in range (3):
    if (lista_faltas[1][c]) == (menos_faltas):
        print ("Pais: ", lista_faltas[0][c], "- Número de faltas= ", lista_faltas[1][c])

#Exercicio feito em aula com auxilio do professor(ar).

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 3) uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um
# programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde
# as informações em uma matriz (lista dentro de lista) . Ao final, o programa deve informar:
# 1) De quem foi a melhor volta da prova, e em que volta.
# 2) Classificação final em ordem crescente.
# 3) Qual foi a volta com a média mais rápida.

# Desafio realizado com Abner Guimarães Silveira e Henrique Dalmagro

# Criando a matriz vazia para armazenar os tempos de cada volta
matriz_tempos = []

# Loop para inserir os tempos de cada volta de cada corredor
for corredor in range(6):
    print(f"Corredor {corredor+1}:")
    tempos_corredor = []  # Lista para armazenar os tempos de um corredor específico
    for volta in range(10):
        tempo = int(input(f"Tempo da volta {volta+1}: "))
        tempos_corredor.append(tempo)
    matriz_tempos.append(tempos_corredor)

# Variáveis para armazenar informações relevantes
melhor_volta = float('inf')  # Inicializa com um valor alto para comparação
corredor_melhor_volta = 0
volta_melhor_volta = 0
classificacao_final = []

# Calculando a melhor volta e a classificação final
for corredor in range(6):
    soma_tempos = sum(matriz_tempos[corredor])  # Calcula a soma dos tempos do corredor
    media_tempos = soma_tempos / 10  # Calcula a média dos tempos do corredor

    # Verifica se é a melhor volta até o momento
    if min(matriz_tempos[corredor]) < melhor_volta:
        melhor_volta = min(matriz_tempos[corredor])
        corredor_melhor_volta = corredor + 1
        volta_melhor_volta = matriz_tempos[corredor].index(melhor_volta) + 1

    # Insere o corredor na classificação final
    classificacao_final.append((corredor + 1, media_tempos))

# Ordena a classificação final com base na média dos tempos
classificacao_final.sort(key=lambda x: x[1])

# Imprime as informações solicitadas
print(f"\nMelhor volta da prova: Corredor {corredor_melhor_volta}, Volta {volta_melhor_volta}")
print("Classificação final:")
for posicao, corredor in enumerate(classificacao_final):
    print(f"{posicao+1}º lugar: Corredor {corredor[0]}")
print(f"Volta com a média mais rápida: Volta {classificacao_final[0][0]}")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 4) Leia uma matriz (lista dentro de lista) 5 x 10 que se refere respostas de 10 questões
# de múltipla escolha, referentes a 5 alunos. Leia também um vetor (lista simples) de 10 posições
# contendo o gabarito de dasrespostas que podem ser a, b, c ou d. Seu programa devera comparar
# as respostas de cada candidato com o gabarito e emitir um vetor (lista simples) denominado
# resultado, contendo a pontuação correspondente a cada aluno.

# Matrizes
matrizRespostas = []
respostasAluno = [] 
pontuacaoAlunos = []

# Listas
gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']

# Contadores
pontuacao = 0

for a in range(5):
    print(f"Aluno {a + 1}:")
    for q in range(10):
        resposta = input(f"Resposta da questão {q + 1}: ")
        respostasAluno.append(resposta)
    matrizRespostas.append(respostasAluno)


for a in range(5):  
    for q in range(10):
        if matrizRespostas[a][q] == gabarito[q]:
            pontuacao += 1
    pontuacaoAlunos.append(pontuacao)


print("Pontuação dos alunos:")
for a in range(5):
    print(f"Aluno {a + 1}: {pontuacaoAlunos[a]}")
