from array import array

def add(arrays, value):
    lengh = len(arrays)
    tempArray = array('i', [0 for _ in range(lengh + 1)]) # Crie um tempArray maior que o array de origem
    
    for i in range(0, lengh):
        tempArray[i] = arrays[i] # Copie o valor da matriz para tempArray
        
    tempArray[lengh] = value # Insira o valor para o último índice
    
    return tempArray

def main():
    arrays = array('i', [90,70,50,80,60,85])
    arrays = add(arrays,75) # Anexar 75 à matriz]
    
    #imprimir todas as matrizes
    length = len(arrays)
    for i in range(0, length):
        print(arrays[i], ",", end="")
    

if __name__ == "__main__":
    main()