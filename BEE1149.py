soma = 0
i=0
d_input = [int(x) for x in input().split()]
a = d_input[0]
for elem in d_input[1::]:
    if elem>0:
        n=elem
while i<=n-1:
    soma += a+i
    i+=1
print(soma)