def avalia_perfeito(dt_input):
    soma=0
    for elem in range(1,dt_input):
        if dt_input%elem==0:
            soma+=elem
    if soma==dt_input:
        return f'{dt_input} eh perfeito'
    else:
        return f'{dt_input} nao eh perfeito'

i = int(input())
j = 0

while j<i:
    print(avalia_perfeito(int(input())))
    j+=1
