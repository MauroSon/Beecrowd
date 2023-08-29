x = int(input())
y = int(input())
if x<y:
    for elem in range(x+1,y):
        if elem%5==2 or elem%5==3:
            print(elem)
else:
    for elem in range(y+1,x):
        if elem%5==2 or elem%5==3:
            print(elem)