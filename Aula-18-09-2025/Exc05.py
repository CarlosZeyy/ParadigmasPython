caixaEletronico = []
valor = ""
saque = 0

while valor != 0:
    valor = float(input("Digite um valor: "))
    saque += valor
    caixaEletronico.append(saque)

print(f"Total sacado: {caixaEletronico[-1]}")