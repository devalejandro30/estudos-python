from datetime import datetime

# Classes 
# utilizadas para criar objetos
# objetos são partes dentro de uma Class
# Class são utilizadas para agrupar dados e funções,
# podendo reutlizar

class Funcionarios:
   # Construtor
   # self <objeto.parâmetro> -> não importa a quantidade de objetos sempre será trocado 
   # pelo self

   def __init__(self, nome, sobrenome, ano_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.ano_nascimento = ano_nascimento

   def nome_completo(self):
      return self.nome + ' ' + self.sobrenome
   
   def idade_funcionario(self):
      ano_atual = datetime.now().year
      self.ano_nascimento = int(ano_atual - self.ano_nascimento)
      return self.ano_nascimento
    
#<nomeo_bjeto> = <classe_do_objeto>
# forma de criar um objeto 

usuario1 = Funcionarios('Roberto','Moré', 2009)  
usuario2 = Funcionarios('Theo', 'Montecito', 2022)

print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))




