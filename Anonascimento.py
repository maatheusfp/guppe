"""
a intenção do programa é dizer exatamente o ano de nascença a partir da idade e data de aniversário levnado em
consideração que hoje é dia 03/05/2021
"""

nome = input('Qual seu nome?')
print(f'Seja bem vindo(a) {nome}')
idade = input('Quantos anos você tem?')
mes = int(input('Qual o mês do seu aniversário?'))
dia = int(input('Qual o dia do seu aniversário?'))
if mes > 5:
    print(f'Você nasceu em {2020 - int(idade)}')
elif mes < 5:
    print(f'Você nasceu em {2021 - int(idade)}')
elif mes == 5:
    if dia > 3:
        print(f'Você nasceu em {2020 - int(idade)}')
    else:
        print(f'Você nasceu em {2021 - int(idade)}')
