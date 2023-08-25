def verify(data_input):
    result=''
    if data_input==0:
        return 'NULL'
    if data_input%2==0:
        result+='EVEN'
    else:
        result+='ODD'
    result+=' '
    if data_input<0:
        result+='NEGATIVE'
    else:
        result+='POSITIVE'
    return result
n = int(input())
for elem in range(0,n):
    data_input=int(input())
    print(verify(data_input))