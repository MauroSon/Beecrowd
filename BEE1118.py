def calculate():
    valido=0
    media=0
    while valido!=2:
        n=float(input())
        if n>=0 and n<=10:
            valido+=1
            media+=n
        else:
            print('nota invalida')
    print(f'media = {media/2:.2f}')
    asw = ''
    while asw!='1' and asw!='2':
        print('novo calculo (1-sim 2-nao)')
        asw = input()
    return asw
asw = calculate()
while asw=='1':
    asw = calculate()
