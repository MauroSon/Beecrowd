def avg(n1,n2,n3):
    result = (n1*2+n2*3+n3*5)/10
    return result
n = int(input())
i=0
while i<n:
    n1,n2,n3 = map(float,input().split())
    print(f'{avg(n1,n2,n3):.1f}')
    i+=1