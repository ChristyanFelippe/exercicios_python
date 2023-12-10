'''
def celsius_kelvin():
    celsius = int(input('Digite um valor em Celsius : '))
    kelvin = celsius + 273
    return kelvin

print(f"O valor é de {celsius_kelvin()}")
'''

'''
Uma função recursiva

def celsius_kelvin():
    celsius = int(input('Digite um valor em Celsius : '))
    kelvin = celsius + 273
    print(f"{kelvin}")
    sair = input("Desejar sair ? responda 'sim' ou 'nao' : ")
    if sair == 'sim':
        return 'Acabou'
    else:
        celsius_kelvin()

print(f"{celsius_kelvin()}")

'''


def aprendendo_inrange():
    i = 0
    while i < 100000:
        i += 1
        print(f"{i}")

aprendendo_inrange()
