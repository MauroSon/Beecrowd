x = int(input())
z = int(input())
i=1
x_v=x
while z<=x:
    z=int(input())
while x<=z:
    x+=(x_v+i)
    i+=1
print(i)
