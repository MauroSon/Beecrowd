def raiz(n):
    if n == 0 :
        return 0
    else:
        return (1/(6+raiz(n-1)))
n = int(input())
print(f'{3+raiz(n):.10f}')
