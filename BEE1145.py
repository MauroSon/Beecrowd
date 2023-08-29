x,y = map(int,input().split())
i=1
while i<=y:
    cont=0
    for elem in range(0,x):
        if elem<x-1:
            print(i,end='')
            print(' ',end='')
        else:
            print(i,end='')
        i+=1
    print()