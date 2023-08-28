n=int(input())
i=0
while i<n:
    impar=0
    n1,n2 = map(int,input().split())
    if n1<n2:
        for elem in range(n1+1,n2):
            if elem%2!=0:
                impar+=elem
    else:
        for elem in range(n2+1,n1):
            if elem%2!=0:
                impar+=elem
    print(impar)
    i+=1