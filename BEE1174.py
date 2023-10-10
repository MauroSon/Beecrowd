i=0
while True:
    try:
        n = float(input())
        if n<=10:
            print(f'A[{i}] = {n}')
            i+=1
        else:
            i+=1
    except:
        break
