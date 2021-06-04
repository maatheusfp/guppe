""" O intuito do programa é calcular o valor da multa por quilo excedente de peixe
"""
peso = float(input('Qual o peso do peixe?'))
if peso > 50.00:
    excesso = peso - 50
    excesso = float(excesso)
    multa = excesso * 4
    multa = float(multa)
    print(f'A multa é de {multa} reais')
else:
    print('Não precisará pagar multa')
