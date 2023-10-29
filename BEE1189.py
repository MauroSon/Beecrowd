operacao = input()
k=1
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
for elem in range(1,12):
    if elem<6:
        for x in range(0,k):
            soma+=matriz[elem][x]
            cont+=1
        k+=1
    else:
        k-=1
        for y in range(0,k):
            soma+=matriz[elem][y]
            cont+=1
if operacao=='S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/cont:.1f}')
