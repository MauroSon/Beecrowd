operacao = input()
i = 0
matriz = []
k=0
final=1
soma=0
qnt = 0
while i<12:
    j=0
    linha = []
    while j<12:
        linha.append(float(input()))
        j+=1
    matriz.append(linha)
    i+=1
for elem in range(1,len(matriz)):
    k=0
    while k<final:
        soma+=matriz[elem][k]
        k+=1
        qnt+=1
    final+=1
if operacao == "S":
    print(soma)
else:
    print(f'{soma/qnt:.1f}')
    
