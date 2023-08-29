asw='1'
grenal=0
empate=0
interW=0
gremioW=0
while asw=='1':
    inter,gremio = map(int,input().split())
    print('Novo grenal (1-sim 2-nao)')
    if inter==gremio:
        empate+=1
    elif inter>gremio:
        interW+=1
    else:
        gremioW+=1
    grenal+=1
    asw=input()    
print(f'{grenal} grenais\nInter:{interW}\nGremio:{gremioW}\nEmpates:{empate}')
if interW>gremioW:
    print('Inter venceu mais')
elif gremioW>interW:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')