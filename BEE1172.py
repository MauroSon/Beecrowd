i = 0
vector = [0]*10
while i<10:
    vector[i] = int(input())
    if vector[i]<=0:
        vector[i]=1
    i+=1
for elem in range(len(vector)):
    print(f'X[{elem}] = {vector[elem]}')
