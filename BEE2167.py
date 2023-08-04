n = int(input())
x = 0
leitura = map(int,input().split())    
leitura = list(leitura)
def checador(leitura):
    for c in range(1,len(leitura)):
        if c != len(leitura): #Checa se é o ultimo elemento
            if leitura[c]<leitura[c-1]: #O atual é menor que o anterior?
                return c+1
    return 0
print(checador(leitura))
