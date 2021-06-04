""" questão 11 da lista estrutura de decisão
"""
salario = input('Qual o seu salário?')
salario = float(salario)
if salario <= 280.00:
    reajuste = 0.20 * salario
    reajuste = float(reajuste)
    reajustado = salario + reajuste
    reajustado = float(reajustado)
    print(f'Seu salário é de {salario}, sofrerá um aumento de 20% \n O valor do aumento será de {reajuste},'
          f'o que deixa o seu salário com o novo valor de {reajustado}')
elif 700 >= salario >= 280:
    reajuste = 0.15 * salario
    reajuste = float(reajuste)
    reajustado = salario + reajuste
    reajustado = float(reajustado)
    print(f'Seu salário é de {salario}, sofrerá um aumento de 15% \n O valor do aumento será de {reajuste},'
          f'o que deixa o seu salário com o novo valor de {reajustado}')
elif 1500 >= salario >= 700:
    reajuste = 0.10 * salario
    reajuste = float(reajuste)
    reajustado = salario + reajuste
    reajustado = float(reajustado)
    print(f'Seu salário é de {salario}, sofrerá um aumento de 10% \n O valor do aumento será de {reajuste},'
          f'o que deixa o seu salário com o novo valor de {reajustado}')
else:
    reajuste = 0.05 *salario
    reajuste = float(reajuste)
    reajustado = salario + reajuste
    reajustado = float(reajustado)
    print(f'Seu salário é de {salario}, sofrerá um aumento de 5% \n O valor do aumento será de {reajuste},'
          f'o que deixa o seu salário com o novo valor de {reajustado}')
