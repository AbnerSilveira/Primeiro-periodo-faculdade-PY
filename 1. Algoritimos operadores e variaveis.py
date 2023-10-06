#1)Apresente uma solução algorítmica escrita na Python para os problemas abaixo apresentados.
#a) Crie uma variável de atribua a ela o valor de uma hora inteira. O algoritmo deve processar a conversão dessa hora em minutos e segundos e imprimir na tela essas conversões. 

horas = int(input("Digite quantas horas deseja converter:"))
minutos = (horas * 60)
segundos = (minutos * 60)

print(horas, "horas equivalem a" ,minutos, "minutos, que respectivamente equivalem a", segundos, "segundos")

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#b) Crie uma variável que receba um valor que é pago por um produto, um segundo valor que é o preço do produto e retorne em outra variável o troco a ser dado. Considere que o valor pago será igual ou maior que o valor do produto.

valorProduto = float(input("Qual o valor do produto:"))
pago = float(input("Qual valor pago pelo cliente:"))


troco = valorProduto - pago
trocoVerdadeiro = troco *-1
if pago < valorProduto:
    print("valor pago insuficiente")
else:
    print(trocoVerdadeiro,"de troco")

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#c) Crie duas variáveis que guarde dois números inteiros, e imprimar o quociente e o resto da divisão inteira entre eles. 

num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite um numero inteiro:"))
quociente = num1/ num2 

print("Seu quociente sera de", quociente)

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#d) Uma variável que guarde o salário fixo de um vendedor, outra o total ($) de vendas por ele efetuadas e outra o percentual de comissão que ele ganha sobre o total vendido. O algoritmo deve imprimir a comissão do vendedor e o seu salário final.

vendedor = str(input("Digite seu nome: "))
totalVendido = int(input("Quantos produtos foram vendidos:"))
percentualComicao = 50/100
precoCamisa = 25
salarioVendedor = 1500

todasCamisas = totalVendido*precoCamisa
percentualRecebido = todasCamisas*percentualComicao
salarioTotal = salarioVendedor + percentualRecebido

print(vendedor,"receberá",salarioVendedor,"mais o percentual de sua comição,",percentualRecebido,", totalizando um salario de",salarioTotal)

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#e) Crie 3 variáveis para guardar três notas informadas por um aluno e exiba a sua média aritmética.

Jorjinho = int(input("Digite a nota de Jorjinho:"))
Juninho = int(input("Digite a nota de Juninho:"))
Joaozinho = int(input("Digite a nota de Joaozinho:"))
mediaAritimetica = (Juninho + Jorjinho + Joaozinho) / 3

print("A média entre Jorjinho, Juninho e Joãozinho é de", mediaAritimetica)

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#f) Um motorista deseja colocar no seu tanque X reais de gasolina. Crie uma variável que guarde o preço do litro da gasolina e o valor que o motorista possui para colocar a gasolina. Imprima quantos litros de gasolina o motorista conseguiu colocar no tanque. 

precoLitro = float(input("Informe o preço do litro da gasolina: "))
valorDisponivel = float(input("Informe o valor disponível para colocar gasolina: "))
litrosGasolina = valorDisponivel / precoLitro

print("Quantidade de litros de gasolina: ", litrosGasolina)

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#g) O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que receba em uma variável o peso (em gramas) do prato montado pelo cliente. O algoritmo deve imprimir o valor que o cliente deve pagar pelo comida . Assuma que a balança já desconte o peso do prato.

pesoPratoGramas = float(input("Informe o peso do prato montado (em gramas): "))
valorPagar = pesoPratoGramas / 1000 * 12

print("Valor a pagar pelo prato: R$", valorPagar)

print("-------------------------------------------------------------------------------------------------------------------------------------------")


#h) Escreva um algoritmo para guarde em 4 variáveis o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e imprimir o percentual que cada um representa em relação ao total de eleitores.

totalEleitores = int(input("Informe o número total de eleitores: "))
votosBrancos = int(input("Informe o número de votos em branco: "))
votosNulos = int(input("Informe o número de votos nulos: "))
votosValidos = int(input("Informe o número de votos válidos: "))

percentualBrancos = (votosBrancos / totalEleitores) * 100
percentualNulos = (votosNulos / totalEleitores) * 100
percentualValidos = (votosValidos / totalEleitores) * 100


print("Percentual de votos em branco:", percentualBrancos, "%")
print("Percentual de votos nulos:", percentualNulos, "%")
print("Percentual de votos válidos:",percentualValidos, "%")

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#i) Crie um algoritmo que irá guardar em uma variável um número inteiro. O algoritmo deve imprimir o antecessor e sucessor desse número.

num = int(input("Digite um numero inteiro:"))
antecessor = num - 1
sucessor = num + 1

print("O antecessor de ", num, "é ", antecessor, "e seu sucessor é ", sucessor)

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#j) Crie um algoritmo que guarde em variáveis o nome de uma pessoa e o ano de nascimento dela. algoritmos deve retornar o nome da pessoa e a sua idade

nome= str(input("qual seu nome: "))
data= int(input("em que ano vc nasceu? "))
ano= int(input("em que ano estamos? "))
idade = ano-data

print(nome, "você tem", idade, "anos.")

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#k) Faça um algoritmos que guarde em um variáveis o peso e a altura de uma pessoa. O algoritmos deve retornar o nome e o IMC (Índice de Massa Corporal) dessa pessoa. 

nome = input("Informe o nome da pessoa: ")
peso = float(input("Informe o peso da pessoa (em kg): "))
altura = float(input("Informe a altura da pessoa (em metros): "))
imc = peso / (altura ** 2)

print("Nome da pessoa:", nome)
print("IMC (Índice de Massa Corporal):", imc)

