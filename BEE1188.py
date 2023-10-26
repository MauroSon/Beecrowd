operacao = input()
j=7
k=5
i=0
matriz=[]
soma = 0
cont=0
while i<12:
    linha = []
    l=0
    while l<12:
        linha.append(float(input()))
        l+=1
    matriz.append(linha)
    i+=1
for elem in range(7,12):
    for x in range(k,j):
        soma+=matriz[elem][x]
        cont+=1
    k-=1
    j+=1
if operacao=='S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/cont:.1f}')
