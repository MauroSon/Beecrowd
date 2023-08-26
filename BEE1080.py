i=0
pos=1
maior=0
posmaior=0
while i<100:
    n=int(input())
    if pos==1:
        maior=n
    else:
        if n>maior:
            maior=n
            posmaior=pos
    pos+=1
    i+=1
print(maior)
print(posmaior)