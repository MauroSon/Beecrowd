x = int(input())
y = int(input())
soma=0
if x<y:
    for elem in range(x,y+1):
        if elem%13!=0:
            soma+=elem
else:
    for elem in range(y,x+1):
        if elem%13!=0:
            soma+=elem
print(soma)