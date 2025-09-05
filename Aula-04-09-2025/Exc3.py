nomes = []
quantidadeNomes = int(input("Digite a quantidade de nomes que vai digitar: "))

for i in range(quantidadeNomes) :
    nome = input(f"Digite o {i + 1}° nome: ")
    nomes.append(nome)

print(f"Lista de nomes: {nomes}")

nomes.reverse()
print(f"Lista de nomes invertidos: {nomes}")
