print ("***ENTRADAS***")
nome = str(input("informe o nome/n: "))
Id = int(input("informe a idade/n: "))
print("*********")
print("Tipos de clientes")
print("1 - vip")
print("2 - comum")
tpc = int(input("Informe o numero do seu tipo de cliente/n: "))
print("********")
print("Tipos de regiões")
print("1 - Norte")
print("2 - Nordeste")
print("3 - Sul")
print("4 - Sudeste")
print("5 - Contro Oeste")
tpr = int(input("informe o numero da sua região/n: "))

#Região Norte
if ((tpc == 1) and (tpr == 1)):
  valorPassagem = 500
elif ((tpc == 2) and (tpr == 1)):
    valor_passagem = 700

#Região Nordeste
elif ((tpc == 1) and (tpr == 2)):
  valorPassagem = 1000
elif ((tpc == 2) and (tpr == 2)):
    valorPassagem = 1200
#Região Sul
elif ((tpc == 1) and (tpr == 3)):
    valorPassagem = 1500
elif ((tpc == 2) and (tpr == 3)):
    valorPassagem = 1700

#Região Sudeste
elif ((tpc == 1) and (tpr == 4)):
  valorPassagem = 800
elif ((tpc == 2) and (tpr == 4)):
  valorPassagem = 400
#Região Centro Oeste
elif ((tpc == 1) and (tpr == 5)):
  valorPassagem = 1300
elif ((tpc == 2) and (tpr == 5)):
  valorPassagem = 920

#verificacão
if ((Id >= 5) and (Id <= 10)):
  desconto = (valorPassagem * 10/100)
elif (Id > 65):
  desconto = (valorPassagem * 50/100)
elif (Id <= 1):
  desconto = (valorPassagem - valorPassagem)
else:
  desconto = 0

print(nome, "valor o valor da passagem é de R$", (valorPassagem - desconto), "Reais")