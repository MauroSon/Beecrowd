entrace = [int(x) for x in input().split()]
result = str(entrace[1]/entrace[0])
result2 = str(entrace[0]/entrace[1])
indice = result.find('.')
indice2 = result2.find('.')
if result[indice+1]=='0' and entrace[1]!=0:
    print('Sao Multiplos')
elif result2[indice2+1]=='0' and entrace[0]!=0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
