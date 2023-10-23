times = int(input())
i=0
while i<times:
    ano=0
    pa,pb,ga,gb = [float(x) for x in input().split()]
    while pb>=pa:
        pb+=int(pb*(gb/100))
        pa+=int(pa*(ga/100))
        ano+=1
        if ano>100:
            print('Mais de 1 seculo.')
            break
    if ano<=100:
        print(f'{ano} anos.')
    i+=1
