def fibo(entrace):
    i=2
    anteAnterior = 0
    anterior = 1
    list_fibo = [0,1]
    if entrace==0:
        return 0
    elif entrace==1:
        return 1
    else:
        while i<=entrace:
            list_fibo.append(list_fibo[anterior]+list_fibo[anteAnterior])
            anterior+=1
            anteAnterior+=1
            i+=1
        return list_fibo[entrace]
i = 0
times = int(input())
while i<times:
    entrace = int(input())
    print(f'Fib({entrace}) = {fibo(entrace)}')
    i+=1
