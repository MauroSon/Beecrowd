entrace = [int(x) for x in input().split(' ')]
sorteado = entrace[:]

sorteado.sort()

for i in range(len(sorteado)):
    print(sorteado[i])
print()
for i in range(len(entrace)):
    print(entrace[i])
