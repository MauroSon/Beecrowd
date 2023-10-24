operacao = input()
i = 0
matriz = []
k=11
soma=0
qnt=0

while i<12:
    j=0
    linha = []
    while j<12:
        linha.append(float(input()))
        j+=1
    matriz.append(linha)
    i+=1
    
for _ in range(len(matriz)-1):
    for elem in range(0,k):
        soma+= matriz[_][elem]
        qnt+=1
    k-=1
    
if operacao == "S":
    print(soma)
else:
    print(f'{soma/qnt:.1f}')
    
