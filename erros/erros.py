# try e except
# não para o programa, mensagens customizadas ao encontrar o erro

try: # se testar isso dq e encontrar um IndexError
     letras = ['a', 'b', 'c'] 
     print(letras[3])
except IndexError: 
     print('Index não existe') # mande esta mensagem

# try:  
#    <cógido> se isso der errado 
# exepct <erro>: e for esse erro
#   <cógido>   faça isso

# exemplo 

try:
    valor = int (input('Digite o valor do seu produto: '))
    print(valor)
except ValueError: # aqui sempre precisa ter o erro que espero que aconteça
     print('Precisa ser necesariamente um número')
finally:
     print('código OK')


#else:    # se não teve o erro
#     print('lUsuário digitou um valor correto')

# add else e finally

# else aparece quando try está OK