from array import array

def main():
    arrays = array('i',[90,70,50,80,60,85]) ##Cria uma matriz de tipo int
    
    lenght = len(arrays) # O comprimento da matriz
    
    for i in range (0,lenght):
        print(arrays[i],",", sep="",end="")
        
        
if __name__ == "__main__":
    main()