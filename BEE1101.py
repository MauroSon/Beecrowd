n1,n2=map(int,input().split())
while n1>0 and n2>0:
    soma=0
    if n1<n2:
        for elem in range(n1,n2+1):
            print(elem ,end=' ')
            soma+=elem
        print(f'Sum={soma}')
    else:
        for elem in range(n2,n1+1):
            print(elem, end=' ')
            soma+=elem
        print(f'Sum={soma}')
    n1,n2=map(int,input().split())