

def isEven(n):
    if (n % 2):
        return False
    else:
        return True

if __name__ == '__main__':
    n = int(input().strip())
    result_func = isEven(n) # Até aqui ok
    if (2 <= n) and (5 >= n) and result_func:
        print("Not Weird")
    elif (6 <= n) and (20 >= n) and result_func:
        print("Weird")
    elif (20 < n) and result_func:
        print("Not Weird")
    else:
        print("Weird")