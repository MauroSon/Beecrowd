first_type = input()
scnd_type = input()
third_type = input()
if first_type == 'vertebrado':
    if scnd_type == 'ave':
        if third_type == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if third_type == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if scnd_type=='inseto':
        if third_type =='hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if third_type == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')