n = int(input())
x=0
while x<n:
    result = []
    name = input()
    dificult = float(input())
    salto = [float(x) for x in input().split()]
    salto = (sum(salto)-min(salto)-max(salto))*dificult
    result.append(name)
    result.append(f'{salto:.2f}')
    print(*result)
    x+=1
