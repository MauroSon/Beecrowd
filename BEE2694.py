n = int(input())
x = 0
soma=0
while x<n:
    string = input()
    stringvazia = ''
    for c in range(0,len(string)):
        if ord(string[c])>=47 and ord(string[c])<=57:
            stringvazia += string[c]
        else:
            stringvazia += ' '
    n1,n2,n3 = map(int,stringvazia.split())
    soma = n1+n2+n3
    x+=1
    print(soma)
