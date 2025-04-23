# altura, largura, rendimento

largura = int(input('Qual a largura da parede? '))
altura = int(input('Qual a altura da parede? '))
rendimento_lata = int(input('Qual o rendimento da lata de tinta? '))

def calculo_tinta():
    quantidade_latas = largura * altura / rendimento_lata
    
    print(f'Você precisa comprar {quantidade_latas} latas de tinta')
 
calculo_tinta()
