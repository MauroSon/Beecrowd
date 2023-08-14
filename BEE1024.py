qnt = int(input())
i=0
while i<qnt:
    new_ph=''
    n_new=''
    ph = input()
    for elem in ph:
        if elem.isalpha():
            new = ord(elem)+3
            new_ph+=chr(new)
        else:
            new_ph+=elem
    new_ph = new_ph[::-1]
    part = new_ph[len(new_ph)//2:]
    for elem in part:
        new = ord(elem)-1
        n_new+=chr(new)
    print(new_ph[:len(new_ph)//2]+n_new)
    i+=1