codigo, qtd = map(int,input().split())
preço = [4, 4.5, 5,2,1.5]
valor = preço[codigo-1]*qtd
print(f'Total: R$ {valor:.2f}')
