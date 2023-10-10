while True:
    try:
        def data_evaluate(data):
            parenteses = 0
            for elem in data:
                if elem=='(':
                    parenteses+=1
                elif elem==')':
                    parenteses-=1
                if parenteses==-1:
                    return 'incorrect'
            if parenteses!=0:
                return 'incorrect'
            else:
                return 'correct'
        print(data_evaluate(input()))
    except EOFError:
        break
