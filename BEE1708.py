a1,a2 = map(int,input().split())
dif = a2 - a1
contador = 1
while a2 > dif:
    a2 -= dif
    contador +=1
print(contador)
