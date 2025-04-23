# Estrutura de dados (listas)

# Armazena mais de uma informorção em variáveis
# Manter a sequencia dos dados de uma variavel

cidades = ['Rio de Janeiro', 'Sao Paulo', 'Salvador', 'Goiania']

# forma de mudar o valor dos elementos de uma lista
cidades[0] = 'Brasilia'
cidades.append('Berlim') # add algum element no final da lista
cidades.remove('Salvador')
cidades.insert(2,'Havana') # insert(posição, intem novo)
cidades.sort() # organiza em ordem alfabética
print(cidades)

# concatenando listas

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c','d']

numeros.extend(letras)
print(numeros)

# listas dentro de listas
# lista grande com sublistas

itens = [['intem1','intem2'],['intem3','intem4']]

print(itens[1][1])
print('------------------')

# extraindo variáveis de listas

produtos = ['arroz', 'feijao', 'laranja', 'banana']
#              0         1         2          3

item1, item2, item3, item4 = produtos

print(item1)
print(item2)
print(item3)
print(item4)
print('--------------------')

# looping dentro de uma lista

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R${x}.')
    
print('--------------------')

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')

    # agregando duas listas com Zip

    colors = ['amarelo', 'verde', 'azul', 'vermelho']
    valores = [10, 20, 30, 40]

    two_list = zip(cores, valores)

    print(list(two_list))

    
# criar uma lista a partir do input oferecido pelo usúario

frutas_usuario = input('Digite o nome das frutas separadas por vírgula: ')

# separa todos os elementos de uma lista, nesse caso, quando tiver uma vírgula 
# e um espaço
frutas_lista = frutas_usuario.split(', ')
 
print(frutas_lista)