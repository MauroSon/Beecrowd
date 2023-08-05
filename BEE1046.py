entrace = [int(x) for x in input().split()]
if entrace[0]>=entrace[1]:
    entrace[0]-=24
    result = entrace[1]-entrace[0]
else:
    result = entrace[1]-entrace[0]
print(f'O JOGO DUROU {result} HORA(S)')
