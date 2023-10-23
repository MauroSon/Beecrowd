vector = [0]*20
i=0
while i<20:
    vector[i] = input()
    i+=1
vector1 = vector[:(i//2):-1]
vector = vector[(i//2)::-1]
vector1.extend(vector)
for elem in range(len(vector1)):
    print(f'N[{elem}] = {vector1[elem]}')
