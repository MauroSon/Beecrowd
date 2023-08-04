x = float(input())
nc = f'{x:.4E}'
if nc[0] == '-':
    nc = f'{x:.4E}'
else:
    nc = f'+{x:.4E}'
print(nc)
