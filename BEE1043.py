def perimeter(n):
    result = 0
    for elem in n:
        result+=elem
    return result
def area(n):
    result = ((n[0]+n[1])*n[2])/2
    return result
n = [float(x) for x in input().split()]
if n[0]>=n[1]+n[2] or n[1]>=n[0]+n[2] or n[2]>=n[1]+n[0]:
    print(f'Area = {area(n):.1f}')
else:
    print(f'Perimetro = {perimeter(n):.1f}')
