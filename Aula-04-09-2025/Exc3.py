nomes = []

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto nome: ")
nome5 = input("Digite o quinto nome: ")

nomes.append(nome1)
nomes.append(nome2)
nomes.append(nome3)
nomes.append(nome4)
nomes.append(nome5)

print(f"Lista de nomes: {nomes}")

nomes.reverse()
print(f"Lista de nomes invertidos: {nomes}")
