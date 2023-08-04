ida, tempo, fuso = map(int,input().split())
volta = ida + tempo + fuso
if volta == 24:
    print(0)
elif (volta>24):
    volta -= 24
elif volta<0:
    volta +=24
print(volta)
