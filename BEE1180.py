i = int(input())
vector = [int(x) for x in input().split()]
print(f'Menor valor: {min(vector)}')
print(f'Posicao: {vector.index(min(vector))}')
