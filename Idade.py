""" O objetivo do programa é descobrir a idade a partir da data  de nascimento  levando
em consideração que estamos em 04/05/2021
"""
nome = input('Qual seu nome?')
print(f'Seja bem vindo(a) {nome}')
dia = int(input('Qual dia você nasceu?'))
mes = int(input('Qual mês você nasceu?'))
ano = int(input('Qual ano você nasceu?'))
if mes > 5:
    print(f'Você tem {2020 - ano} anos')
elif mes < 5:
    print(f'Você tem {2021 - ano} anos')
else:
    if dia > 4:
        print(f'Você tem {2020 - ano} anos')
    else:
        print(f'Você tem {2021 - ano} anos')
