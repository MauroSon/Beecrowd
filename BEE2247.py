cont = 1
n = int(input())
while n != 0:
    faltou = 0
    i = 1
    print(f'Teste {cont}')
    while i <= n:
        n1, n2 = map(int,input().split())
        faltou = n1 - n2+faltou
        print(faltou)
        i+=1
    cont+=1
    print()
    n = int(input())
