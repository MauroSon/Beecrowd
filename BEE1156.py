soma = 0
a=3
b=2
c=1
while a<=39:
    if c==1:
        soma+= 1 + a/b
        c-=1
    else:
        soma+= a/b
    a+=2
    b*=2
print(f'{soma:.2f}')
