def somar():
    print('Esta função irá somar valores')

def multi():
    print('Esta função irá multiplicar valores')


def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
