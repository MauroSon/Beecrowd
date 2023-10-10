i = 0
vector = [0]*10
vector[0] = int(input())
while i<9:
    vector[i+1]=vector[i]*2 
    i+=1
for elem in range(len(vector)):
    print(f'N[{elem}] = {vector[elem]}')
