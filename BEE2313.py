def verificar():
    if (l1==l2!=l3) or (l2==l3!=l1) or (l1==l3!=l2):
        tri = "Isoceles"
    elif (l1!=l2!=l3):
        tri = "Escaleno"
    else:
        tri = "Equilatero"
    return tri
def retangulo():
    ret = (l1**2+l2**2==l3**2) or (l2**2+l3**2==l1**2) or (l1**2+l3**2==l2**2)
    if ret == True:
        ret = "S"
    else:
        ret = "N"
    return ret

l1, l2, l3 = map(int, input().split())
validar = (l3<l1+l2) and (l1<l3+l2) and (l2<l1+l3)
if validar==True:
    tri = verificar()
    print(f"Valido-{tri}")
    ret = retangulo()
    print(f"Retangulo: {ret}")
else:
    print("Invalido")
    
    
