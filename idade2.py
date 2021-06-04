"""
O objetivo desse programa é receber a data de nascimento junta e, a partir disso, dar  a idade
"""
nome = input('Qual seu nome?')
print(f'Seja bem vindo(a) {nome}')
dia, mes, ano = input('Qual sua data de nascimento?').split()
dia = int(dia)
mes = int(mes)
ano = int(ano)
if mes > 5:
    print(f'Você tem {2020 - ano} anos')
elif mes < 5:
    print(f'Você tem {2021 - ano} anos')
else:
    if dia > 4:
        print(f'Você tem {2020 - ano} anos')
    else:
        print(f'Você tem {2021 - ano} anos')
