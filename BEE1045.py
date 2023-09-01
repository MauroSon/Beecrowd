data_input = [float(n) for n in input().split()]
data_input.sort(reverse=True)
if data_input[0]>=data_input[1]+data_input[2]:
    print('NAO FORMA TRIANGULO')
else:
    if data_input[0]**2==data_input[1]**2+data_input[2]**2:
        print('TRIANGULO RETANGULO')
    elif data_input[0]**2>data_input[1]**2+data_input[2]**2:
        print('TRIANGULO OBTUSANGULO')
    elif  data_input[0]**2<data_input[1]**2+data_input[2]**2:
        print('TRIANGULO ACUTANGULO')
    if data_input[0]==data_input[1] and data_input[1]==data_input[2]:
        print('TRIANGULO EQUILATERO')
    elif data_input[0]==data_input[1] and data_input[1]!=data_input[2] or data_input[1]==data_input[2] and data_input[0]!=data_input[2] or data_input[0]==data_input[2] and data_input[2]!=data_input[1]:
        print('TRIANGULO ISOSCELES')
        
