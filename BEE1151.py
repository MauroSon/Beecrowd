def fibo(n):
    fibo_list = [0,1,1]

    i=2
    if n>2:
        while i<n:
            fibo_list.append(fibo_list[len(fibo_list)-1]+fibo_list[len(fibo_list)-2])
            i+=1
    for elem in range(0,n):
        if elem==n-1:
            print(fibo_list[elem])
        else:
            print(fibo_list[elem], end=' ')
n=int(input())
fibo(n)
