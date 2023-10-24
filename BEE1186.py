operacao = input()
i=0
matriz=[]
soma=0
cont = 0
k=10
while i<12:
    linha = []
    j=0
    while j<12:
        linha.append(float(input()))
        j+=1
    matriz.append(linha)
    i+=1

for x in range(1,12):
    for elem in range(11,k,-1):
        soma+=matriz[x][elem]
        cont+=1
    k-=1
if operacao=='S':
    print(soma)
else:
    print(f'{soma/cont:.1f}')
