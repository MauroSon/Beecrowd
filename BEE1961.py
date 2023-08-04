pulo,n_cano = map(int,input().split())
def sapador():
    variavel = 0
    cano = [int(x) for x in input().split()]
    for c in range(0,len(cano)-1):
            if abs(cano[c+1]- cano[c])<=pulo:
                variavel+=1 
    return variavel
variavel = sapador()
if variavel+1 >= n_cano:
    print('YOU WIN')
else:
    print('GAME OVER')
