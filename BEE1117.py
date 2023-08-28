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