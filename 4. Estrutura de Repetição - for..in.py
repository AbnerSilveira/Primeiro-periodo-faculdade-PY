# 1) Faça um algoritmo que guarde em uma lista as notas finais de 10 alunos.
# O algoritmo deve calcular retornar:
# - Quantidade de alunos aprovados. Considere nota de aprovação igual ou maior que 7.
# - A soma das notas dos alunos que obtiveram média entre 5 e 10.
# - A média das notas dos alunos aprovados.
# - A maior média entre os alunos aprovados.
# - A menor média entre os alunos reprovados.


notas = []
for I in range(10):
    alunos = float(input("Informe as notas: "))
    notas.append(alunos)

maiornotaap = 0
menornotarp = 0
somaap = 0
contap = 0
soma510 = 0
mediarp = 0


for item in notas:
    if item >= 7:
        contap += 1
        somaap = somaap + item

    if item > maiornotaap:
        maiornotaap = item
    else:
        if (item < menornotarp) or (menornotarp == 0):
            menornotarp = item

    if (item >= 5) and (item <= 10):
        soma510 += item

mediaap = somaap / contap

print("Quantidade de alunos aprovados: ", contap)
print("Média das notas dos alunos aprovados: ", mediaap)
print("Maior nota entre os alunos aprovados: ", maiornotaap)
print("Menor nota entre os alunos reprovados: ", menornotarp)
print("Soma das notas ente 5 e 10 ", soma510)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# 2) Faça um algoritmo que registre em uma lista a sequência dos números sorteados na mega sena e em outra lista os números de um bilhete jogado por uma determinada pessoa. O algoritmo deve retornar se a pessoa ganhou ou não na mega sena, além de retornar quantos e quais números ela acertou.


jogados = []
for i in range(6):
    jgd = float(input("Informe os números jogados: "))
    jogados.append(jgd)

sorteados = [23, 5, 12, 31, 33, 4]
acertou = [0, 0, 0, 0, 0, 0]

cont = 0

for i in range(6):
    for j in range(6):
        if jogados[i] == sorteados[j]:
            cont = cont + 1
            acertou[i] = jogados[i]
if cont == 6:
    print("você ganhou na mega sena")
    print("Numeros que você acertou foram", acertou)
else:
    print("Não foi dessa vez: a quantidade de números que você acertou foi:", cont)
    print("Numeros que você acertou foram", acertou)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# 3) Faça um algoritmo onde o usuário irá alimentar 3 listas com as seguintes informações de 10 chuveiros: código, tensão e corrente .O algoritmo deverá :
# a) Calcular em uma nova lista a potência de cada chuveiro. Considere potência tensão x corrente.
# b) Imprimir os códigos dos chuveiros com seus respectivas potências .
# c) Calcular e imprimir a média das potências.
# d) Calcular e imprimir quantos chuveiros possuem tensões maiores que 50.
# e) Verificar e imprimir o código e a potência do chuveiro mais econômico.
# f) Verificar e imprimir o código e a potência do chuveiro menos econômico.

# listas
codigo = []
tensao = []
corrente = []
potencia = []

# contadores
potenciaChuveiros = 0
quantidadeChuveiros = 0
chuveirosTensaoAlta = 0
potenciaMaisEconomica = 0
potenciaMenosEconomica = 0
codigoMenosEconomico = 0
codigoMaisEconomico = 0

for X in range(10):
    cdg = float(input("Informe o código do chuveiro: "))
    tns = float(input("Informe a tensão do chuveiro: "))
    crt = float(input("Informe a corrente do chuveiro: "))
    codigo.append(cdg)
    tensao.append(tns)
    corrente.append(crt)

for P in range(10):
    ptc = tensao[P] * corrente[P]
    potencia.append(ptc)

print(
    "O chuveiro de código:",
    codigo,
    "tem respectivamente as potencias de: ",
    potencia,
    "W.",
)

for PC in potencia:
    potenciaChuveiros += PC
    quantidadeChuveiros += 1

mediaPotenciaChuveiros = potenciaChuveiros / quantidadeChuveiros

print("A média da potencia dos chuveiros é de: ", mediaPotenciaChuveiros)

for T in tensao:
    if T >= 50:
        chuveirosTensaoAlta += 1
print("A soma dos chuveiros com tensão maior ou igual a 50 é de:", chuveirosTensaoAlta)

for i, PE in enumerate(potencia):
    if (PE < potenciaMaisEconomica) or (potenciaMaisEconomica == 0):
        potenciaMaisEconomica = PE
        codigoMaisEconomico = codigo[i]
print(
    "O chuveiro de mais economico, com potência de: ",
    potenciaMaisEconomica,
    "é o chuveiro de código: ",
    codigoMaisEconomico,
)

for i, PN in enumerate(potencia):
    if PN > potenciaMenosEconomica:
        potenciaMenosEconomica = PN
        codigoMenosEconomico = codigo[i]
print(
    "O chuveiro de menos economico, com potência de: ",
    potenciaMenosEconomica,
    "é o chuveiro de código: ",
    codigoMenosEconomico,
)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 4)Uma empresa de compras através da Internet decidiu realizar uma pesquisa entre os seus clientes para determinar o perfil dos mesmos.. Faça um algoritmo que alimente 4 listas com seguintes dados de 20 clientes: nome, idade, sexo (masculino/feminino) e se possuem acesso ou não à Internet. O algoritmo deverá :
# a. Calcular e imprimir a média de idade dos clientes;
# b. Separar em duas listas distintas os nome das mulheres e dos homens.
# c. Imprimir a lista com o nome dos homens e a lista com o nome das mulheres
# d. Calcular o percentual de mulheres que possuem acesso a Internet.
# e. O nome e a idade do homem mais velho que tem acesso a Internet
# f. O nome e a idade da mulher mais nova.

# listas
nome = []
idade = []
sexo = []
acessoI = []
homens = []
mulheres = []

# contadores
somaIdade = 0
quantidadePessoas = 0
contSexo = 0
contMulherInt = 0
maioridade = 0
nomemaior = ""
menoridade = 0
nomemenor = ""

for Y in range(20):
    nm = str(input("Insira seu nome: "))
    id = int(input("Insira sua idade: "))
    sx = str(input("Insira seu sexo (M = Masculino/F = Feminino): "))
    acssI = str(input("Insira se possui acesso a  interner (Sim/ Não): "))

    nome.append(nm)
    idade.append(id)
    sexo.append(sx)
    acessoI.append(acssI)

for I in idade:
    somaIdade += I
    quantidadePessoas += 1

mediaIdade = somaIdade / quantidadePessoas

print("A média de idade das pessoas é de:", mediaIdade)

for N, S in enumerate(sexo):
    if S == "M":
        homens.append(nome[N])
    else:
        mulheres.append(nome[N])

print("Homens: ", homens, ", Mulheres: ", mulheres)

for i in range(20):
    if ((sexo[i] == "F") and (acessoI[i] == "Sim")):
        contMulherInt = contMulherInt+1
print ("O percentual de mulheres com acesso a internet é:", contMulherInt/len(mulheres)*100, "%")

for i in range(20):
    if ((sexo[i] == "M") and (acessoI[i] == "Sim")):
        if idade[i] > maioridade:
            maioridade = idade[i]
            nomemaior = nome[i]
print ("O nome do homem mais velho com acesso a internet é: ", nomemaior)

for i in (range(20)):
    if (sexo[i] == "F"):
        if (idade[i] < menoridade) or (menoridade == 0):
            menoridade = idade[i]
            nomemenor = nome[i]
print ("O nome da mulher mais nova é ", nomemenor, "e ela possui ", menoridade, "anos")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 5) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

#Listas
temp=[]
meses = ["Janeiro", "Fevereiro","Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mesesAcima = []

# Contadores
mediaAnual = 0


for i in (range(12)):
    t = float (input(f"Informe a temperatura de {i}:"))
    temp.append(t)

mediaAnual = sum(temp) / len(temp)
print ("A média anual é de", mediaAnual)

for i in temp:
    if (temp[i] > mediaAnual):
        mesesAcima.append(temp[i])
print ("Meses que possuem temperatura acima da média anual:", mesesAcima)


print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# Exercício 6) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a) "Telefonou para a vítima?"
# b) "Esteve no local do crime?"
# c) "Mora perto da vítima?"
# d) "Devia para a vítima?"
# e) "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# Contadores
cont = 0

#Listas
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = []

for i in perguntas:
    p = str(input(f"{i} (responda com Sim/Não)"))
    respostas.append(p)

for i in respostas:
    if (i == "Sim"):
        cont+= 1

if (cont==2):
    print ("Suspeita")
elif (cont>=3) and (cont<=4):
    print ("Cumplice")
elif (cont>=5):
    print ("Assasino")
else:
    print ("Inocente")