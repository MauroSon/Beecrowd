dinheiro = int(input())
print(dinheiro)
valor = [50,20,10,5,2,1]
def contarDinheiro(dinheiro, valor):
    resto = dinheiro%valor
    text = f'{dinheiro//valor} nota(s) de R$ {valor:.2f}'
    print(text.replace('.',','))
    return resto

resto = contarDinheiro(dinheiro,100)
for elem in valor:
    resto = contarDinheiro(resto,elem)