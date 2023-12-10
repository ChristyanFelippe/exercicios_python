from icecream import ic


def teste_dicionario():
    lista = []
    for i in range(1):
        dicionario = dict(nome=input("Insira o nome : "), sexo=input("Insira M ou S para Masculino ou Feminino. : "),
                          idade=int(input("Insira a idade : ")))
        # esporte=input("Esporte Favorito : ")
        ic(dicionario)
        lista.append(dicionario)
    ic(lista)
    return lista
    
def verificar_sexo(lista):
    print(lista.sexo)
    


lista = teste_dicionario()

contador_de_homens = 0
soma_das_idades = 0