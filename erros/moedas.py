total_centavos = int(input('Digite a quantidade de centavos desejada a seguir: '))

real = 100
moeda1 = 50
moeda2 = 25
moeda3 = 10
moeda4 = 5
moeda5 = 1


resto1 = total_centavos % real
inteiro1 = total_centavos // real

resto2 = resto1 % moeda1
inteiro2 = resto1 // moeda1

resto3 = resto2 % moeda2
inteiro3 = resto2 // moeda2

resto4 = resto3 % moeda3
inteiro4 = resto3 // moeda3

resto5 = resto4 % moeda4
inteiro5 = resto4 // moeda4


resto6 = resto5 % moeda5
inteiro6 = resto5 // moeda5


print(f'para o valor {total_centavos} centavos, a menor quantidade de moedas é de {inteiro1} moedas de 1 real,'
      f' {inteiro2} moedas de 50 centavos, {inteiro3} moedas de 25 centavos, {inteiro4} moeda de 10 centavos '
      f'e {inteiro5} moedas de 5 centavos e {inteiro6} moedas de 1 centavo')