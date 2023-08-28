i=0
n=int(input())
while i<n:
    n1,n2=map(int,input().split())
    if n2==0:
        print('divisao impossivel')
    else:
        print(f'{n1/n2:.1f}')
    i+=1