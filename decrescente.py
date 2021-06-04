""" o intuito do programa é mostrar os números recebidos em ordem decrescente """

num1, num2, num3 = input('Digite três números').split()
if num1 > num2 > num3:
    print(f'{num1}, {num2}, {num3}')
elif num1 > num3 > num2:
    print(f'{num1}, {num3}, {num2}')
elif num2 > num1 > num3:
    print(f' {num2}, {num1}, {num3}')
elif num2 > num3 > num1:
    print(f'{num2}, {num3}, {num1}')
elif num3 > num2 > num1:
    print(f'{num3}, {num2}, {num1}')
else:
    print(f'{num3}, {num1}, {num2}')
