linhaProcurada = int(input())
Operacao = input()
matriz = []
i = 0
while i<12:
    j=0
    linha = []
    while j<12:
        linha.append(float(input()))
        j+=1
    matriz.append(linha)
    i+=1
if Operacao=='S':
    print(sum(matriz[linhaProcurada]))
else:
    print(sum(matriz[linhaProcurada])/12)
