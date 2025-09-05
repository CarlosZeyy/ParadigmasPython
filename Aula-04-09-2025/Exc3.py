nomes = []

for i in range(5) :
    nome = input(f"Digite o {i + 1}° nome: ")
    nomes.append(nome)

print(f"Lista de nomes: {nomes}")

nomes.reverse()
print(f"Lista de nomes invertidos: {nomes}")
