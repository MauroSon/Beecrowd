n1 = int(input())
n2 = int(input())
impar = 0
if n1>n2:
    for elem in range(n2,n1+1,2):
        impar+=elem
else:
    for elem in range(n1,n2+1,2):
        impar+=elem
print(impar)