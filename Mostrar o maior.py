num1, num2, num3 = input('digite 3 números').split()
if num1 > num2 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')
