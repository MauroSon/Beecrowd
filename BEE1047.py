hi,mi,hf,mf = map(int,input().split())
result=((hf*60)+mf)-((hi*60)+mi)
if(result<=0):
    result+=24*60
hourf = result//60
minutef = result%60
print(f'O JOGO DUROU {hourf} HORA(S) E {minutef} MINUTO(S)')
