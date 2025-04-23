# 15451

n = int(input('Digite um número de 5 dígitos: '))
d1 = n // 10000  # saída 1
n1 = n % 10000 # 5451
d2 = n1 // 1000 # 5
n2 = n % 1000 # 451
d3 = n2 // 100 # 4
n3 = n % 100 # 51
d4 = n3 // 10 # 5
n4 = n3 % 10 #1 

if d1 == n4 and d2 == d4:
    print('O número digitado é um palíndromo')
else:
    print('Não é um palíndromo')
    
'''
Faça um programa que leia um número inteiro entre 0 e 9999 e
escreva o seu valor por extenso

Faça um programa que leia três coordenadas num espaço 2D e
indique se formam um triângulo, juntamente com o seu tipo
(equilátero, isósceles e escaleno)
– Equilátero: todos os lados iguais
– Isósceles: dois lados iguais
– Escaleno: todos os lados diferentes
'''