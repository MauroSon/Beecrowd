n=int(input())
i=0
def primo(dt_input):
    for elem in range(2,dt_input):
        if dt_input%elem==0:
            return f'{dt_input} nao eh primo'
    return f'{dt_input} eh primo'            
while i<n:
    print(primo(int(input())))
    i+=1
