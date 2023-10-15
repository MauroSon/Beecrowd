vectorImpar = []
vectorPar = []
i=0
while i<15:
    entrace = int(input())
    if len(vectorPar)==5:
        for elem in range(len(vectorPar)):
            print(f'par[{elem}] = {vectorPar[elem]}')
        vectorPar = []
    if len(vectorImpar)==5:
        for elem in range(len(vectorImpar)):
            print(f'impar[{elem}] = {vectorImpar[elem]}')
        vectorImpar = []
    if entrace%2==0:
        vectorPar.append(entrace)
    else:
        vectorImpar.append(entrace)
    i+=1
if len(vectorImpar)!=0:
    for elem in range(len(vectorImpar)):
        print(f'impar[{elem}] = {vectorImpar[elem]}')
if len(vectorPar)!=0:
    for elem in range(len(vectorPar)):
        print(f'par[{elem}] = {vectorPar[elem]}')
