#RUNTIME ERROR
def media(qnt,cons):
    cons = cons//qnt
    text = f'{qnt}-{cons}'
    return text
n = int(input())
while n!= 0:
    sorted_cons = ''
    consumos = []
    i=1
    cont = 0
    print(f'Cidade# {i}: ')
    while cont<n:    
        qnt, cons = map(int,input().split())
        consumos.append(media(qnt,cons))
        cont+=1
    sorted_cons = sorted(consumos, key=lambda x:x[1])
    print(sorted_cons)
    n = int(input())
    i+=1