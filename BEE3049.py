Base = int(input())
Topo = int(input())
AreaFelix = (((Base)+(Topo))*70)/2
AreaMarzia = (70*160)-AreaFelix
if AreaFelix>AreaMarzia:
    print('1')
elif AreaMarzia>AreaFelix:
    print('2')
else:
    print('0')
