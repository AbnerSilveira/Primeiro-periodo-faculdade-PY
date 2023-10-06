# Exercício 1:
# Uma companhia quer verificar entre os seus empregados quais estão qualificados para a
# aposentadoria. Para estar em condições de se aposentar, o empregado deverá atender a pelo
# menos um dos seguintes requisitos:
# 1 - Ter no mínimo 65 anos de idade.
# 2 - Ter trabalhado no mínimo 30 anos.
# 3 - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# São dados de entrada: o número do empregado, o ano de seu nascimento e o ano de seu ingresso
# na companhia. O programa deverá calcular e retornar:
# 1 - A idade e o tempo de trabalho de cada empregado, exibindo a mensagem: “Requerer
# aposentadoria” ou “Não requerer aposentadoria”;
# 2 - Quantos funcionários estão qualificados para a aposentadoria e quantos não estão
# qualificados;
# 3 - A média de tempo de serviço dos funcionários qualificados para a aposentadoria.
# Obs.: O algoritmo será encerrado pelo usuário

# Listas
numero = []
nascimento = []
anoTrab = []

# Contadores
i = 0
contA = 0
contNA = 0
somaTempo = 0
mediaTempo = 0
anoAtual = 2023

resp = int(input("Deseja Iniciar? (Sim, Não): "))

while (resp == "Sim"):
    num = int(input("Informe o número do empregado: "))
    numero.append(num)
    nsc = int(input("Informe o ano de nascimento: "))
    nascimento.append(nsc)
    at = int(input("Informe o ano de ingresso na companhia: "))
    anoTrab.append(at)

    idade = anoAtual - nascimento[i]

    tempoServico = anoAtual - anoTrab[i]

    if ((idade >= 65) or (tempoServico >= 30)) or (
        (idade >= 60) and (tempoServico >= 25)
    ):
        print(
            "Idade: ",
            idade,
            " | Tempo de serviço: ",
            tempoServico,
            "| Situação: Requer aposentadoria",
        )
        contA += 1
        somaTempo += tempoServico
    else:
        print(
            "Idade: ",
            idade,
            " |Tempo de serviço: ",
            tempoServico,
            "|Situação: Não requer aposentadoria",
        )
        contNA += 1

    i += 1
    resp = int(input("Deseja Continuar? (Sim, Não): "))

mediaTempo = somaTempo / contA

print("Funcionarios a serem aponsentados:", contA)
print("Funcionarios não aptos a aponsentadoria:", contNA)
print("A média de tempo de serviço dos aptos a aponsentadoria:", mediaTempo)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 2:
# Faça um programa que guarde em uma lista o nome e a quantidade de filmes locados por seus
# clientes durante o ano de 2022. Calcule em um outra lista a quantidade de filmes promocionais que
# os clientes possuem direito, considere que para cada 10 filmes locados os clientes terão direito uma
# nova locação. O Algoritmo deverá apresentar o nome do cliente que ganhou o maior números de
# locações promocionais e o nome do cliente que ganhou menos locações promocionais.
# Obs.: O algoritmo será encerrado pelo usuário


# Listas
nome = []
quant = []
promo = []

# Contadores
i = 0
maior = 0
menor = 0
nomemaior = ""
nomeMenor = ""

resp = int(input("Deseja iniciar? (Sim, Não):"))

while (resp == "Sim"):
    n = (input("Informe o nome:"))
    nome.append(n)
    q = int(input("Informe a quantidade de filmes locados:"))
    quant.append(q)
    pro = quant[i] / 10
    promo.append(pro)
    
    if (promo[i] > maior):
        maior = promo[i]
        nomeMaior = nome[i]
    
    if ((promo[i] < menor) or (menor == 0)):
        menor = promo[i]
        nomeMenor = nome[i]
    
    i = i + 1
    resp = int(input("Deseja continuar? (Sim, Não): "))

print ("---------------LISTAS---------------")
print ("Lista de Nomes: ", nome)
print ("Lista de Quantidade: ", quant)
print ("Lista de promoções: ", promo)
print ("------------------------------------")
print ("O Cliente que ganhou o maior número de promoções foi: ", nomeMaior)
print ("O Cliente que ganhou o menor número de promoções foi: ", nomeMenor)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 3:
# Leia em 4 listas distintas os dados de vários alunos: O nome do aluno, a nota da n1, a nota da n2 e
# a nota do Exame Semestral. O algoritmo deve:
# 1) Calcular em uma 5ª lista a média final do aluno, sabendo que o peso das notas
# são: N1= 20%, N2= 35% e Exame Semestral= 45%.
# 2) Calcular em uma 6ª lista se o aluno está aprovado ou reprovado, sabendo que a
# média final de aprovação é 5.0.
# 3) Permitir que se possa fazer uma pesquisa pelo nome do aluno e retornar dessa
# pesquisa: o nome do aluno, a sua média final e se o aluno está aprovado ou
# reprovado.
# 4) Retorne: O nome do aluno que apresentou a maior média. Registre também a
# posição dentro da lista onde se encontra esse aluno.
# 5) Retorne: nome do aluno que apresentou a menor média. Registre também a
# posição dentro da lista onde se encontra esse aluno.
# 6) Retorne: A quantidade de alunos aprovados e reprovados.
# 7) Retorne: A média geral da turma.

# Listas
nome = []
nota1 = []
nota2 = []
semestral = []
media = []
situacao = []

# Contadores
i = 0
maiorMedia = 0
menormedia = 0
nomeMaior = ""
nomeMenor = ""
posicaoMenor = 0
posicaoMaior = 0
contap = 0
contrp = 0
mediaGeral = 0
resp2 = "Sim"

resp1 = str(input("Deseja iniciar? (Sim, Não): "))

while (resp1 == "Sim"):
#entradas
    n = (input("Informe o nome:"))
    nome.append(n)
    n1 = float(input("Informe a nota da N1"))
    nota1.append(n1)
    n2 = float(input("Informe a nota da N2"))
    nota2.append(n2)
    ex = float(input("Informe a nota do Exame Semestral"))
    semestral.append(ex)
    md = float ((nota1[i] * 0.20) + (nota2[i] * 0.35) + (semestral[i] * 0.45))
    media.append(md)
    if ((media[i]) >= 5):
        st = str ("Aprovado")
        situacao.append(st)
        contap += 1
    else:
        st = str ("Reprovado")
        situacao.append(st)
        contrp += 1

    i = i + 1
    resp1 = str(input("Deseja continuar? (Sim, Não): "))
print ("-----------------------------------------------------------------")


while (resp2 == "Sim"):
    pesq = str(input("Qual o nome que deseja pesquisar? "))
    for c in range(len(media)):
        if (nome[c] == pesq):
            print ("Aluno:", nome[c], "| Média: ", media[c], "|Situação:", situacao[c])
            break
    resp2 = str (input("Deseja pesquisar outro nome? (Sim, Não): "))
print ("-----------------------------------------------------------------")

for i in range(len(media)):
    if (media[i] > maiorMedia):
        maiorMedia = media[i]
        nomeMaior = nome[i]
        posicaoMaior = i
    if (media[i] < menorMedia) or (menorMedia == 0):
        menorMedia = media[i]
        nomeMenor = nome[i]
        posicaoMenor = i

print ("Aluno com maior média:", nomeMaior, "|media:", maiorMedia,
"|posição:", posicaoMaior)
print ("Aluno com menor média:", nomeMenor, "|media:", menorMedia,
"|posição:", posicaoMenor)
print ("-----------------------------------------------------------------")

print ("Quantidade de aprovados: ", contap)
print ("Quantidade de reprovados: ", contrp)
print ("-----------------------------------------------------------------")

mediaGeral = sum(media) / len(media)
print ("A média geral da turma é: ", mediaGeral)