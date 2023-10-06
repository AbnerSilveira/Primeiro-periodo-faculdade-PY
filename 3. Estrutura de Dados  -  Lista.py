# 1) Exercicios base de listas:
# a) Crie uma lista vazia . Imprima a lista.

lista = []
print(lista)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# b) Crie uma lista “idade” com a idade de 10 pessoas. Imprima a lista.

idade = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# c) Solicite ao usuário uma nova idade e insira na lista. Imprima a lista.

Id = []
idadeAd = int(input("Qual sua idade: "))
if idadeAd not in Id:
    Id.append(idadeAd)
    print(Id)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# d) Crie uma nova lista “nome” com o nome de 6 pessoas.Imprima a lista.

nome = ["Abner", "Jorjinho", "Juninho", "joãozinho", "Jotinha", "Nathan"]
print(nome)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# e) Crie uma nova lista “nome_idade” com o conteúdo das duas listas anteriores. Imprima a lista.

nome_idade = [
    "Abner",
    "Jorjinho",
    "Junonho",
    "joãozinho",
    "Jotinha",
    "Nathan",
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
]
print(nome_idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# f) Imprima a lista “idade” e imprima o 5º elemento dessa lista.

print(idade[4])

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# g) Imprima a lista “idade” e imprima o elemento que está na posição/ índice 5 dessa lista.

print(idade[5])

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# h) Imprima a lista “idade” e imprima o elemento que está na posição/indice -5 dessa lista.

print(idade[-5])

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# i) Imprima a lista “nome_idade “ e imprima a 4º idade dessa lista

print(nome_idade[9])

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# j) Imprima a lista “nome” e informe quantos elementos essa lista possui.

print(nome.count)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# k) Concatene a lista “nome” com a lista “idade”

nomeIdade = nome + idade
print(nomeIdade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# l) Crie duas cópias da lista idade e imprima o resultado.

print(idade * 2)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# m) Imprima a lista “nome” e verifique se o nome Joana consta ou não nessa lista.

print(nome)
"joana" in nome

# meu VSCode demonostra valores booleanos

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# n) Imprima a lista idade e retorne a maior idade, a menor idade e a soma de todas as idades dessa lista.

print(min(idade))
print(max(idade))
print(sum(idade))

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# o) Insira na lista “nome” um novo nome e na lista “idade” uma nova idade. Imprima as duas listas.

nome.append("Jeremias")
idade.append("27")
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# p) Insira um novo nome no início da lista “nome” e uma nova idade no início da lista “idade”. Imprima as listas.

nome.insert(0, "Jabotão")
idade.insert(0, 78)
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# q) Imprima lista “nome” e a lista “idade" e remova a última idade da lista “idade”e o último nome da lista “nome”. Imprima as duas listas.

print(nome)
print(idade)
nome.pop()
idade.pop()
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# r) Imprima a lista “nome” e a lista “idade”. Remova o nome que está na posição/indice 3 da lista “nome” e remova a idade que está na posição 2 da lista idade. Imprima novamente as listas para checagem.

print(nome)
print(idade)
nome.pop(3)
idade.pop(2)
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# s) Informe um nome e uma idadade existente nas listas “nome” e “idade” e remova esses elementos dessas listas.

print(nome[3])
print(idade[1])
nome.pop(3)
idade.pop(1)
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# t) Coloque em ordem crescente as duas listas (nome/idade). Imprima as listas.

nome.sort()
idade.sort()
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# u) Imprima as duas lista (nome/idade) em ordem reversa.

nome.reverse()
idade.reverse()
print(nome)
print(idade)

print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)

# v) Verifique quantas vezes um determinado número inteiro aparece na lista idade

idade.count(19)
