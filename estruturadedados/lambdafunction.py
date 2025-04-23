from sys import getsizeof # pega o tamanho de algo

# é uma função (pequena) sem nome
# pode ter vários argurmentos e somente 1 expressão
# utilizada dentro de outras funções
# código mais 'clean'

def somar(x):
    return x + 10

print(somar(2))

# lambda <argumentos>: expressão
# subfunção

somar10 = lambda x, y: x + y + 10
print(somar10(2, 7))

def add(g):
    func2 = lambda g: g + 10
    return func2(g) * 4

print(add(6))

# map function -> aplica uma função a um iterable, por item

lista1 = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, lista1)))

numbers = [3, 6, 9, 21]

print ((list( map(lambda y: y / 3, numbers))))

# filter function -> filtra os items

valores = [10, 12, 34, 44, 57]

print(list(filter(lambda x: x > 20, valores)))

 # list comprehension ***
 # criar uma nova lista a partir de uma existente

# selecionar somente as frutas que contêm com a letra b e botar numa nova lista

frutas1 = [ 'abacate', 'banana', 'morango', 'kiwi', 'abacaxi']


# for iten in frutas1:
#    if 'n' in iten:
#        frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'w' in iten]
print(frutas2)

# values = []

# for r in range(6):
#    values.append(r * 10)

# print(values)

values = [r * 10 for r in range(6)] 
print(values)

# generator expressions
# forma mais rápida de listas, dicionários e etc
# menos memória alocada, valores em bytes


numeros = [z * 10 for z in range(100000)] # gasta 8856 bytes
print(type(numeros))
print(getsizeof(numeros))

# generator
numeros = (z * 10 for z in range(100000)) # gasta 200 bytes
print(type(numeros))
print(getsizeof(numeros))