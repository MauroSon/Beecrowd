a,b,c = map(float,input().split())
areatri = a*c/2
areacirc = 3.14159*c**2
areatrap = (a+b)*c/2
areaquad = b**2
arearet = a*b
print(f'TRIANGULO: {areatri:.3f}')
print(f'CIRCULO: {areacirc:.3f}')
print(f'TRAPEZIO: {areatrap:.3f}')
print(f'QUADRADO: {areaquad:.3f}')
print(f'RETANGULO: {arearet:.3f}')