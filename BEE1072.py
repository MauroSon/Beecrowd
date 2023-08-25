n = int(input())
ins=0
out=0
for elem in range(0,n):
    data_input=int(input())
    if data_input>=10 and data_input<=20:
        ins+=1
    else:
        out+=1
print(f'{ins} in\n{out} out')