n1,n2,n3 = map(int,input().split())
maiorAB = (n1+n2+abs(n1-n2))/2
maiorABC = (maiorAB+n3+abs(maiorAB-n3))/2
print(f'{maiorABC:.0f} eh o maior')