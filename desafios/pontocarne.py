# dempendendo da temperatura indicar o ponto da carne.
# o usuário deve indicar a temperatura

temperatura_carne = int(input('Qual é a temperatura da carne? '))

if temperatura_carne < 48:
    print('cozinhar por mais alguns minutos')
elif temperatura_carne in range(48, 53):
    print('selada')
elif temperatura_carne in range(54, 59):
    print('ao ponto para bem')
elif temperatura_carne in range(60, 64):
    print('ao ponto')
elif temperatura_carne in range(65, 70):
    print('ao ponyo para bem')
elif temperatura_carne >= 71:
    print('bem passada')
