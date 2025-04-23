# dicionários
# utiliza índice no formato de keys e de values
# aceita str, int, float, bool...

aluno = {
    'nome': 'Ana',
    'idade': 16, 
    'nota_final': 'A',
    'aprovacao': True,
    'materias': ['Fcg',  'Md', 'Fac', 'Prog', 'Lab']

 }

#          key   value   key     value     key     value    key    value

# manipulando dados no dicionários
aluno.update({'nome': 'Alejandro','idade': 21,'nota': 'B'}) 
# pegar 
print(aluno.get('endereco', 'não existe'))
del aluno['idade'] # remover algo do dicionário
print(aluno)

# looping dentro do dicionário

for keys, values in aluno.items():
    print(keys, values)

print(aluno.get('materias'))
print(len(aluno)) # imprime o número de keys
