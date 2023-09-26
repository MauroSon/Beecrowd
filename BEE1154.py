n = int(input())
i=0
media=0
while n>=0:
    media+=n
    n=int(input())
    i+=1
media/=i
print(f'{media:.2f}')
