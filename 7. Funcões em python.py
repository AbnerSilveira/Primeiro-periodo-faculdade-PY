# 1) Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def imprimeMenor(a, b):
    if a < b:
        print(a)
    elif a > b:
        print(b)
    else:
        print("Os números são iguais.")

imprimeMenor(0, 5)
imprimeMenor(10, 3)
imprimeMenor(42, 42)


# 2) Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.


def imprimeSinal(n):
    if n < 0:
        print("Negativo")
    else:
        print("Positivo")
imprimeSinal(-1)
imprimeSinal(5)

# 3) Escreva uma função para imprimir o valor absoluto de um número.

def imprimeValorAbsoluto(n):
    if n < 0:
        n = -n
    print(n)

imprimeValorAbsoluto(-5)
imprimeValorAbsoluto(10)
imprimeValorAbsoluto(-1)

# 4) Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, 
# chamado limite.

def somaMaiorQueLimite(a, b, limite):
    if a + b > limite:
        return True
    else:
        return False
    
print(somaMaiorQueLimite(10, 5, 15))

# #5) Escreva uma função que recebe um número como parâmetro e\ para cada número menor que o parâmetro, a função imprime
# "Fizz" se o número for múltiplo de três, imprime "Buzz" se o número for múltiplo de cinco, e imprime "FizzBuzz" se o número
# for múltiplo de três e cinco. Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. Note que, ao
# contrário das funções anteriores, sua função não deve retornar nada. Ela precisa simplesmente imprimir o que foi pedido.

def fizzBuzz(n):
    for num in range(n):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

print(fizzBuzz(16))

# 6) Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).

def converte_nota_em_conceito(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    elif nota >= 40:
        return "E"
    else:
        return "F"
    
print(converte_nota_em_conceito(65))

# 7) Escreva uma função que recebe como entrada uma lista de números e retorna True se um número passado como parâmetro está presente na lista.

def pesquisaElemento(numeros, numeroProcurado):
    for numero in numeros:
        if numero == numeroProcurado:
            return True
        return False
print(pesquisaElemento([1, 10, 20, 30, 50, 100], 30))

# 8) Escreva uma função que recebe como entrada uma lista ordenada de números e retorna o índice do
# primeiro elemento maior que um elemento limite. Se nenhum elemento da lista for maior que o limite desejado, retorne o valor -1.

def retornaPrimeiroMaior(numeros, limite):
    i = 0
    while i < len(numeros):
        if numeros[i] > limite:
            return i
        i += 1
    return -1
print(retornaPrimeiroMaior([1, 10, 20, 30, 50, 100], 10))
print(retornaPrimeiroMaior([1, 10, 20, 30, 50, 100], 200))