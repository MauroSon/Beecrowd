i = int(input())
j = 0

while j<i:
    hash_map = {}
    m,c = map(int,input().split())
    data = [int(x) for x in input().split()]
    for elem in range(0,m):
        hash_map[elem]=[]
    for elem in data:
        hash_map[elem%m].append(elem)
    for elem in range(len(hash_map)):
        if hash_map[elem]==[]:
            print(f'{elem} -> \\')
        else:
            temp = hash_map[elem]
            print(f"{elem} -> ",end='')
            print(*temp, sep=' -> ',end='')
            print(' -> \\')
    if j!=i-1:
        print()
    j+=1
