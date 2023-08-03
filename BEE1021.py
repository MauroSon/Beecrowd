def contar_nota(N,valorR):
    qtd = int(N/valorR)
    print(f'{qtd} nota(s) de R$ {valorR:.2f}')
    resto = N%valorR
    return resto

def contar_moeda(M,valorM):
    qtd = int(M/valorM)
    print(f'{qtd} moeda(s) de R$ {valorM/100:.2f}')
    resto = (M % valorM)
    return resto

valorR = [100,50,20,10,5,2]
valorM = [100,50,25,10,5,1]

N,M = map(int,input().split("."))


print('NOTAS:')
resto = contar_nota(N,valorR[0])
for r in valorR[1:]:
    resto = contar_nota(resto,r)
M += resto*100
print('MOEDAS:')
resto = contar_moeda(M,valorM[0])
for r in valorM[1:]:
    resto = contar_moeda(resto,r)