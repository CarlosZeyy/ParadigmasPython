precos = []

for i in range(5):
    valor = float(input(f"Digite o {i + 1}° valor: "))
    

    if valor > 50:
        precos.append(valor)

print(f'Valores maiores que 50: {precos}')