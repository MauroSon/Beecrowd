def fibo(n):
    if n==1:
        return 1
    return n*fibo(n-1)
i = int(input())
print(fibo(i))
