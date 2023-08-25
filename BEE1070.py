n = int(input())
if n%2==0:
    for elem in range(n+1,n+12,2):
        print(elem)
else:
    for elem in range(n,n+12,2):
        print(elem)
        