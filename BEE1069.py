data = int(input())
i=0
while i<data:
    diamantes = ''
    diamante_valido = 0
    data_input = input()
    for elem in data_input:
        if elem=='<':
            diamantes+='<'
        elif elem=='>':
            diamantes+='>'
    while '<>' in diamantes:
        diamante_valido+=1
        diamantes = diamantes.replace('<>',"",1)
    print(diamante_valido)
    i+=1
