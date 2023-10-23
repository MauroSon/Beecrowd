i = int(input())
while i!=0:
    if i%2==0:
        j=i+2
        i+=j
        j=j+2
        i+=j
        j=j+2
        i+=j
        j=j+2
        i+=j
    else:
        i+=1
        j=i+2
        i+=j
        j=j+2
        i+=j
        j=j+2
        i+=j
        j=j+2
        i+=j
    print(i)
    i = int(input())
