par=0
impar=0
positivo=0
negativo=0
for elem in range(0,5):
    data_input = float(input())
    if data_input%2==0:
        par+=1
    else:
        impar+=1
    if data_input>0:
        positivo+=1
    elif data_input<0:
        negativo+=1
print(f'{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivo} valor(es) positivo(s)\n{negativo} valor(es) negativo(s)')