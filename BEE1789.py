def lesmador():
    vazio = int(input())
    corrida = [int(x) for x in input().split()]
    if max(corrida)>=20:
        return 3
    elif max(corrida)>=10 and max(corrida)<20:
        return 2
    else:
        return 1
    
while True:
    try:
        print(lesmador())
    except:
        break
