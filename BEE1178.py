n = float(input())
vector = [0]*100
i = 0
while i<100:
    vector[i] = n
    n = n/2
    i+=1
for elem in range(len(vector)):
    print(f'N[{elem}] = {vector[elem]:.4f}')
