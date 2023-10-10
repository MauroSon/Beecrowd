n=int(input())
i=0
while i<n:
    soma=0
    x,y = map(int,input().split())
    if x%2!=0:
        for elem in range(x,2*y+x):
            if elem%2!=0:
                soma+=elem
    else:
        for elem in range(x,2*y+x):
            if elem%2!=0:
                soma+=elem
    print(soma)
    i+=1
