from array import array

# é uma lista imutável -> não pode ser alterada
# tuple utiliza () ao invés de []
# listas consomen mais espaço que tuples

colors_tuple =('amarelo', 'verde', 'azul', 'vermelho')
colors_list =['amarelo', 'verde', 'azul', 'vermelho']

colors_list.append('laranja')

print(colors_tuple)
print(colors_list)

# array (matriz) usa-se quando é preciso de uma lista grande (listas > 10^3)e de tb de performace
# depende do type code 
# estrutura -> <lista> = array ('<type code>' [<elementos da lista>])

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array ('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)

# set (listas)
# mesma estrutua de uma lista mas com {}
# similar a listas, evita itens duplicados e não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)


print(num1 | num2) # (Union) unifica as duas listas retirando os valores repetidos
print(num1 - num2) # (Difference) 
print(num1 ^ num2) # (Symmetric Difference) retira todos os duplicados das duas listas
print(num1 & num2) # (And) imprime os elementos duplicados

s1 = {1, 2, 3, 4, 5, 6}
s1.add(9) # add um elemento
s1.update([7, 8]) # add vários elementos
# remove dá erro se o item removido não está no set, já o discard não

print(s1)