def fibonacci_recursivo(n, lista=[]):
    if n <= 0:
        return lista
    elif n == 1:
        lista.append(0)
        return lista
    elif n == 2:
        lista.append(0)
        lista.append(1)
        return lista
    else:
        lista = fibonacci_recursivo(n - 1, lista)
        lista.append(lista[-1] + lista[-2])
        return lista

def main():
    n = int(input("Digite quantos termos da sequência de Fibonacci você deseja gerar: "))
    fibonacci_list = fibonacci_recursivo(n)
    print("Sequência de Fibonacci com", n, "termos:", fibonacci_list)

if __name__ == "__main__":
    main()
