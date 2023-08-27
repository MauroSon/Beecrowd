n=int(input())
experiment = {'coelho':0,'rato':0,'sapo':0,'total':0}
i=0
while i<n:
    cob,typ = input().split()
    cob = int(cob)
    experiment['total']+=cob
    if typ == 'C':
        experiment['coelho']+=cob
    elif typ == 'R':
        experiment['rato']+=cob
    else:
        experiment['sapo']+=cob
    i+=1
print(f'Total: {experiment["total"]} cobaias\nTotal de coelhos: {experiment["coelho"]}\nTotal de ratos: {experiment["rato"]}\nTotal de sapos: {experiment["sapo"]}\nPercentual de coelhos: {experiment["coelho"]*100/experiment["total"]:.2f} %\nPercentual de ratos: {experiment["rato"]*100/experiment["total"]:.2f} %\nPercentual de sapos: {experiment["sapo"]*100/experiment["total"]:.2f} %')