i=0
media = 0
for elem in range(0,6):
    data_input = float(input())
    if data_input>0:
        i+=1
        media+=data_input
print(f'{i} valores positivos')
print(f'{media/i:.1f}')