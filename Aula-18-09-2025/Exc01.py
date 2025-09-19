camiseta = 39.90
calcas = 99.90

compraCamiseta = int(input("Digite a quantidade da camisetas compradas: "))
compraCalcas = int(input("Digite a quantidade da calças compradas: "))

total = (compraCamiseta * camiseta) + (compraCalcas * calcas)

print(f'Valor total da compra: R$ {round(total, 2)}')