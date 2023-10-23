operacao = input()
i=0
matriz=[]
soma=0
x=1
cont = 0

while i<12:
    linha = []
    j=0
    while j<12:
        linha.append(float(input()))
        j+=1
    matriz.append(linha)
    i+=1

for _ in range(0,11):
    for elem in range(x,12):
        soma+=matriz[_][elem]
        cont+=1
    x+=1
if operacao=='S':
    print(soma)
else:
    print(f'{soma/cont:.1f}')
