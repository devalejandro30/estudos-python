# programa que calcule o fatorial de um dado número

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

x = int(input())
print(factorial(x))