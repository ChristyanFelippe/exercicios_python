'''
1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N
termos da sequência de Fibonacci em uma lista. N é definido pelo usuário. Ao
encontrar os termos, imprimir a lista e finalizar a função.
'''
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    fib(int(10))