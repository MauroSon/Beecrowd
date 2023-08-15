def adjustment(data_input):
    if data_input<=400.00:
        print(f'Novo salario: {data_input+(0.15*data_input):.2f}\nReajuste ganho: {0.15*data_input:.2f}\nEm percentual: 15 %')
    elif data_input<=800.00:
        print(f'Novo salario: {data_input+(0.12*data_input):.2f}\nReajuste ganho: {0.12*data_input:.2f}\nEm percentual: 12 %')
    elif data_input<=1200.00:
        print(f'Novo salario: {data_input+(0.1*data_input):.2f}\nReajuste ganho: {0.1*data_input:.2f}\nEm percentual: 10 %')
    elif data_input<=2000.00:
        print(f'Novo salario: {data_input+(0.07*data_input):.2f}\nReajuste ganho: {0.07*data_input:.2f}\nEm percentual: 7 %')
    else:
        print(f'Novo salario: {data_input+(0.04*data_input):.2f}\nReajuste ganho: {0.04*data_input:.2f}\nEm percentual: 4 %')
adjustment(float(input()))