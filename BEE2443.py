x = 2
n1,n2,n3,n4 = map(int,input().split())
if n2 == n4:
    Cima = n1+n3
    Baixo = n2
else:
    Cima = n1*n4+n3*n2
    Baixo = n2*n4
while (x<=Cima) and (x<=Baixo):
    while Baixo % x == 0 and Cima % x == 0:
        Baixo = Baixo//x
        Cima = Cima//x
    x+=1
print(f'{Cima} {Baixo}')
