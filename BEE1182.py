colunaProcurada = int(input())
operacao = input()
matriz = []
i=0
soma = 0
while i<12:
    j=0
    linha = []
    while j<12:
        linha.append(float(input()))
        j+=1
    matriz.append(linha)
    i+=1
for elem in range(0,12):
    soma+= matriz[elem][colunaProcurada]
if operacao=='S':
    print(soma)
else:
    print(f'{soma/12:.1f}')

