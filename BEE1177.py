n = int(input())
vector = [0]*1000
i = 0
j=0
while i<1000:
    if j<n:
        vector[i]=j
        j+=1
        i+=1
    else:
        j=0
for elem in range(len(vector)):
    print(f'N[{elem}] = {vector[elem]}')
