while True:
    try:
        n  = int(input())
        x=0
        dic = {}
        n_dic = {}
        while x<n:
            nome,preço = input().split()
            preço = int(preço)
            dic[preço] = nome
            x+=1
        n_dic = sorted(dic.items(), key=lambda x:x[0])
        n_dic = dict(n_dic)
        print(*n_dic.values())
    except EOFError:
        break
