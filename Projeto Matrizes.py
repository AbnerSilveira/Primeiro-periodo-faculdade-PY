# Desafio:
# Agora vamos colocar em um menu todas as atividade que
# fizemos da letra “a” até “i” e o usuário irá escolher qual
# atividade quer executar, sendo que ele não pode executar
# nenhuma outra atividade antes de executar a atividade da
# letra “a” que é preencher a matriz.
# Assim que executar a opção desejada, o sistema deve
# permitir que o usuário retorne ao menu principal se
# desejar executar outra opção.
# 13
# *********EXERCÍCIOS COM MATRIZES*******
# ********************************************
# Selecione a opção desejada:
# ********************************************
# 1 – Preencher uma matriz com números inteiros
# 2 – Imprimir a matriz de números inteiros
# 3 – Imprimir a soma dos elementos de cada linha da matriz
# 4 – Imprimir a soma dos elementos de cada coluna damatriz
# 5 – Imprimir a somados elementos da diagonal principal
# 6 – Imprimir a matriz transposta
# 7 – Imprimir quantidade de elementos pares e impares
# 8 – Imprimir a soma de todos os elementos da matriz
# 9 – Imprimir o maior elemento da matriz e onde se encontra
# 0 – Encerrar o Sistema
# ********************************************
# ********************************************


#Tabela para orientacão
print("-----------EXERCÍCIOS COM MATRIZES-----------")
print("------------------------------------------------")
print("Selecione a opção desejada:")
print("------------------------------------------------")
print("1 Preencher uma matriz com números inteiros")
print("2 Imprimir a matriz de números inteiros")
print("3 Imprimir a soma dos elementos de cada linha da matriz")
print("4 Imprimir a soma dos elementos de cada coluna da matriz")
print("5 Imprimir a soma dos elementos da diagonal principal")
print("6 Imprimir a matriz transposta")
print("7 Imprimir quantidade de elementos pares e ímpares")
print("8 Imprimir a soma de todos os elementos da matriz")
print("9 Imprimir o maior elemento da matriz e onde se encontra")
print("0 Encerrar o Sistema")
print("------------------------------------------------")
print("------------------------------------------------")

#Zerando matrisez, listas e contadores
matriz= [[0,0,0],[0,0,0],[0,0,0]]
cont = 0
transposta = [[0,0,0],[0,0,0],[0,0,0]]

#Iniciando casos e esruturas de repeticões
while True:
  #Pedido de opcão do usuario
  opcao = int(input("\nDigite sua opção: "))
  print()
  #Preenchimento obrigatorio da matriz
  if cont == 0 and opcao != 1:
    print("Primeiramente preencha sua matriz")
    print()
    for l in range(3):
      for c in range(3):
        matriz[l][c] = int(input("um numero inteiro: "))
      print()
    cont += 1
    continue
  match opcao:
    case 1:
      #Preencher matriz
      for l in range(3):
        for c in range(3):
          matriz[l][c] = int(input("um numero inteiro: "))
        print()

    case 2:
      #Imprimir matriz
      for l in range (3):
        for c in range (3):
          print (matriz[l][c], "/ ", end = '')
        print()

    case 3:
      #Soma das linhas
      somalinha = 0
      for l in range(3):
        for c in range (3):
         somalinha =(somalinha+matriz[l] [c])
        print("a soma da linha", l, "é:", somalinha)
        print()

    case 4:
      #Soma das colunas
      somacoluna = 0
      for c in range(3):
        for l in range(3):
          somacoluna = (somacoluna + matriz [l] [c])
        print("A soma da coluna", c, "é:", somacoluna)
        print()

    case 5:
      #Soma em diagonal
      somadiagonal = 0
      for l in range(3):
        for c in range(3):
         if (l==c):
            somadiagonal=somadiagonal+matriz[l][c]
      print("A soma dos elementos da diagonal principal é:", somadiagonal)

    case 6:
      #Soma geral
      somageral = 0
      for l in range(3):
        for c in range(3):
          transposta[l][c]=matriz[c][l]
      for l in range(3):
        for c in range(3):
          print (transposta[l][c],"|", end='')
        print()

    case 7:
      #Numeros pares e impares
      contpar=contimpar=0
      for l in range(3):
        for c in range(3):
          if (matriz[l][c]%2==0):
            contpar=contpar+1
          else:
            contimpar=contimpar+1
      print("A quantidade de números pares é:", contpar)
      print("A quantidade de números pares é:",contimpar)

    case 8:
      #Soma geral
      somageral=0
      for l in range(3):
        for c in range(3):
          somageral=(somageral+matriz[l][c])
      print("A soma geral é:", somageral)

    case 9:
      #Maior numero e sua posicão
      maior=0
      linhamaior=0
      colunamaior=0
      for l in range(3):
        for c in range(3):
          if (matriz[l][c]>maior):
            maior=matriz[l][c]
            linhamaior=l
            colunamaior=c
      print("O maior elemento é:", maior)
      print("Sua linha se encontra em:", linhamaior)
      print("Sua coluna se encontra em",colunamaior)

    case 0:
      #Finalizacão da tarefa
      print("Finalizando tarefa")

    case _:
      #Caso de erro
      print("Opção invalida")
      continue
  cont += 1

#Desafio realizado com Abner Guimarães Silveira e Henrique Dalmagro (https://simpler1ick.github.io/), com aplicação de estudos em "match case".