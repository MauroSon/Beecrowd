
def soma():
    n = num[0]*num[3]+num[1]*num[2]
    d = num[1]*num[3]
    return n,d
def sub():
    n = num[0]*num[3]-num[1]*num[2]
    d = num[1]*num[3]
    return n,d
def mult():
    n = num[0]*num[2]
    d = num[1]*num[3]
    return n,d
def div():
    n = num[0]*num[3]
    d = num[1]*num[2]
    return n,d
def reductor(n,d):
    for elem in range(2,d):
        while n%elem==0 and d%elem==0:
            n = n//elem
            d = d//elem
    return n,d
def operation(entrace):
    if entrace[3] == '+':
        return (soma())
    elif entrace[3] == '-':
        return (sub())
    elif entrace[3] == '*':
        return (mult())
    else:
        return (div())
i = 0
qnt = int(input())
while i < qnt:
    entrace = input().split()
    num = map(int,entrace[::2])
    num = list(num)
    n,d = operation(entrace)
    print(f'{n}/{d} = ', end='')
    n,d = reductor(n,d)
    print(f'{n}/{d}')
    i+=1
