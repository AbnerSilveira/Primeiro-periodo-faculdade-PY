# 1) Elabore uma solução algorítmica em PYTHON para os problemas abaixo apresentados:
# a) Escreva um algoritmo que leia dois números e exiba o maior deles

num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite um numero inteiro:"))

if num1 > num2:
    print("O número ", num1, "é maior que o numero ", num2)
elif num1 == num2:
    print("Os dois números são iguais.")
else:
    print("O número ", num2, "é maior que o número ", num1)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# b) Escreva um algoritmo para ler um número inteiro e retornar se ele é maior, igual ou menor que zero.

num = int(input("Digite um número inteiro:"))

if num == 0:
    print("Seu número é nulo.")
elif num > 0:
    print("Seu número é positivo.")
else:
    print("Seu número é negativo.")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# c) Faça um algoritmo que leia um número inteiro e retorne se o número é par o ímpar.

numero = int(input("Digite um número inteiro:"))

if numero % 2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é impar.")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# d) Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 80, menor que 25 ou igual a 40.

Num = int(input("Digite um número inteiro:"))

if Num > 80:
    print("Seu número é maior que 80")
elif Num < 25:
    print("Seu número é menor que 25.")
elif Num == 40:
    print("Seu número é igual a 40.")
else:
    print("Seu número não está entre os requisitos.")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# e) Elabore um algoritmo para testar se uma senha digita é igual a “batatafrita”. Se a senha estiver correta escreva “Acesso permitido”, do contrário emita a mensagem “Você não tem acesso ao sistema”.

senha = str(input("Informe a senha "))

if senha == "batatafrita":
    print("Acesso permitido.")
else:
    print("Você não tem acesso ao sistema.")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# f) Escrever um algoritmo que leia três valores inteiros distintos e os escreva em ordem crescente.

numero1 = int(input("Digite um número inteiro:"))
numero2 = int(input("Digite um número inteiro:"))
numero3 = int(input("Digite um número inteiro:"))

if numero1 < numero2 < numero3:
    print("A ordem crescente dos números são: ", numero1, numero2, numero3)
elif numero1 < numero3 < numero2:
    print("A ordem crescente dos números são: ", numero1, numero3, numero2)
elif numero2 < numero1 < numero3:
    print("A ordem crescente dos números são: ", numero2, numero1, numero3)
elif numero2 < numero3 < numero1:
    print("A ordem crescente dos números são: ", numero2, numero3, numero1)
elif numero3 < numero1 < numero2:
    print("A ordem crescente dos números são: ", numero3, numero1, numero2)
elif numero3 < numero2 < numero1:
    print("A ordem crescente dos números são: ", numero3, numero2, numero1)
else:
    print("Seus números são iguais.")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# g) Escrever um algoritmo para uma empresa que decide dar um reajuste a seus funcionários de acordo com os seguintes critérios:
# . 50% para aqueles que ganham menos do que três salários mínimos;
# .. 20% para aqueles que ganham entre três até dez salários mínimos;
# ... 15% para aqueles que ganham acima de dez até vinte salários mínimos;
# .... 10% para os demais funcionários.

salarioMinimo = 1.320
salarioFuncionario = int(input("Digite seu salário atual:"))

if salarioFuncionario < (salarioMinimo * 3):
    salarioNovo = salarioFuncionario + (salarioFuncionario * 0.5)
    reajuste = "50%"
    aumento = salarioNovo - salarioFuncionario
elif (salarioFuncionario > (salarioMinimo * 3)) and (
    salarioFuncionario <= (salarioMinimo * 10)
):
    salarioNovo = salarioFuncionario + (salarioFuncionario * 0.2)
    reajuste = "20%"
    aumento = salarioNovo - salarioFuncionario
elif (salarioFuncionario > (salarioMinimo * 10)) and (
    salarioFuncionario <= (salarioMinimo * 20)
):
    salarioNovo = salarioFuncionario + (salarioFuncionario * 0.15)
    reajuste = "15%"
    aumento = salarioNovo - salarioFuncionario
else:
    salarioNovo = salarioFuncionario + (salarioFuncionario * 0.1)
    reajuste = "10%"
    aumento = salarioNovo - salarioFuncionario

print(
    "Seu salário levou um reajuste de ",
    reajuste,
    ", ficando atualmente em R$",
    salarioNovo,
    ", levando um aumento de R$",
    aumento,
)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# h) Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor do produto e imprima o valor de venda para o produto

compraProduto = int(input("Por quanto comprou o produto:"))

if compraProduto > 20:
    valorProduto = compraProduto + (compraProduto * 0.45)
    lucro = compraProduto - valorProduto
else:
    valorProduto = compraProduto + (compraProduto * 0.3)
    lucro = compraProduto - valorProduto


print(
    "O valor do produto aumentou para R$",
    valorProduto,
    ", obtendo o lucro de R$",
    lucro,
)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# i) A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%.

precoCarro = int(input("Valor do carro:"))
anoCarro = int(input("Ano do carro:"))

if anoCarro > 2000:
    valorCarro = precoCarro - (precoCarro * 0.07)
    desconto = "7%"
else:
    valorCarro = precoCarro - (precoCarro * 0.12)
    desconto = "12%"

print(
    "O valor do carro é de ",
    precoCarro,
    ",com o desconto de ",
    desconto,
    ", reduziu para ",
    valorCarro,
)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# j) Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.

nume = int(input("Digite um numero inteiro:"))

if (nume >= 100) or (nume <= 200):
    print("Seu número está dentro do intervalo aceito")
else:
    print("Seu número não está dentro do intervalo aceito")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# k) O Botafogo Futebol Clube deseja aumentar o salário de seus jogadores. O reajuste deve obedecer a seguinte tabela:
# SALÁRIO ATUAL (R$)     /     AUMENTO
# 0,00 a 5.000,00        /       20%
# 5.000,01 a 15.000,00   /       10%
# acima de 15.000,00     /       0%
# Escrever um algoritmo que leia o nome e o salário atual de um jogador, e exiba o / nome, o salário atual e o salário reajustado.

nome = str(input("Digite seu nome: "))
salarioAtual = float(input("Digite seu salario atual: "))

if salarioAtual <= 5000:
    salarioFinal = salarioAtual + (salarioAtual * 0.2)
    Reajuste = "20%"
    Aumento = salarioFinal - salarioAtual
    print(
        "Olá",
        nome,
        "seu salario atual de R$",
        salarioAtual,
        ", levou um reajuste de ",
        reajuste,
        "tatalizando R$",
        salarioFinal,
    )
elif (salarioAtual >= 5000.01) and (salarioAtual <= 15000):
    salarioFinal = salarioAtual + (salarioAtual * 0.1)
    Reajuste = "10%"
    Aumento = salarioFinal - salarioAtual
    print(
        "Olá",
        nome,
        "seu salario atual de R$",
        salarioAtual,
        ", levou um reajuste de ",
        reajuste,
        "tatalizando R$",
        salarioFinal,
    )
else:
    print("Olá", nome, "Seu salario não levou reajuste")

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# l) Faça um algoritmo para calcular a conta final de um hóspede de um hotel fictício, considerando que:
# • Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias utilizadas pelo hóspede e o valor do consumo interno do hóspede;
# • O valor da diária é determinado pela seguinte tabela:
# 1. TIPO DO APTO. / 2. VALOR DA DIÁRIA (R$)
# 3.      A        /       4. 150,00
# 5.      B        /       6. 100,00
# 7.      C        /       8. 75,00
# 9.      D        /       10. 50,00
# • O valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da diária;
# • O subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
# • O valor da taxa de serviço equivale a 10% do subtotal;
# • A total geral resulta da soma do subtotal com a taxa de serviço.
# • Escreva a conta final contendo: o nome do hóspede, o tipo do apartamento, o número de diárias utilizadas, o valor unitário da diária, o valor total das diárias, o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total geral.

hospede = str(input("Digite seu nome: "))
tipoAp = str(input("Qual tipo de Ap. o hóspede ficou (Entre os tipos A, B, C ou D): "))
dias = int(input("Quantos dias o hóspede ficou no Ap.: "))
valorConsumo = float(input("Qual o valor de consumo do hóspede: "))

if tipoAp == "A":
    valorAp = 150
    ValorDiarias = dias * valorAp
    subtotal = ValorDiarias + valorConsumo
    valorTS = subtotal * 0.1
    total = subtotal + valorTS
elif tipoAp == "B":
    valorAp = 100
    ValorDiarias = dias * valorAp
    subtotal = ValorDiarias + valorConsumo
    valorTS = subtotal * 0.1
    total = subtotal + valorTS

elif tipoAp == "C":
    valorAp = 75
    ValorDiarias = dias * valorAp
    subtotal = ValorDiarias + valorConsumo
    valorTS = subtotal * 0.1
    total = subtotal + valorTS

elif tipoAp == "D":
    valorAp = 50
    ValorDiarias = dias * valorAp
    subtotal = ValorDiarias + valorConsumo
    valorTS = subtotal * 0.1
    total = subtotal + valorTS

else:
    print()

print(
    "Olá ",
    hospede,
    ", você se hospedou no tipo de Ap. ",
    tipoAp,
    ", e ficou por ",
    dias,
    "dias, cada dia tendo o valor de R$",
    valorAp,
    ", o total das diarias ficou em R$",
    ValorDiarias,
    ", seu consumo interno na hospedaria finalizou em R$",
    valorConsumo,
    ", somando as suas diarias fica R$",
    subtotal,
    "mais a nossa taxa de serviso de 10% ou R$",
    valorTS,
    ", finalizando um total de R$",
    total,
)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)