n=int(input())
alcool=0
gas=0
diesel=0
while n!=4:
    if n in range(1,4):
        if n==1:
            alcool+=1
        elif n==2:
            gas+=1
        elif n==3:
            diesel+=1
        n=int(input())
    else:
        n=int(input())    
print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gas}\nDiesel: {diesel}')