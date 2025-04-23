# filtrar listas

funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}
tem_bike = ['Bruno', 'Melissa']

print('têm carro e trabalha à noite: '+ str(list(tem_carro & turno_noite)))
print('têm carro e trabalha de dia: '+ str(list(tem_carro & turno_dia)))
print('funcionários que não têm carro: '+ str(list((funcionarios - tem_carro))))

lista1 = set(tem_bike).intersection(tem_carro)
print(lista1)