""" o intuito do programa é calcular o peso ideal baseado no sexo da pessoa
"""
sexo = input('Qual o seu sexo?')
altura = input('Qual a sua altura?')
altura = float(altura)
if sexo == "masculino":
    ideal = 72.7 * altura - 58
    ideal = float(ideal)
    print(f'Seu peso ideal é {ideal}')
else:
    ideal = 62.1 * altura - 44.7
    ideal = float(ideal)
    print(f'Seu peso ideal é {ideal}')
