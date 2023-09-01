n=int(input())
while n!=0:
    for elem in range(1,n+1):
        if elem!=n:
            print(elem, end=' ')
        else:
            print(elem)
    n=int(input())