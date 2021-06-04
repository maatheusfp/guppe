""" Ideia do programa é dar melhor custo para ao cliente referente ao quanto ele pintar
 """
area = float(input("Qual será a área pintada?"))
litros_necessarios = area // 6
litros_necessarios = float(litros_necessarios)
litros_ideal = litros_necessarios + 0.1 * litros_necessarios
litros_ideal = float(litros_ideal)
if area < 108:
lata_18litros = litros_ideal // 18.00
lata_18litros = int(lata_18litros)

print(f'{lata_18litros}')
