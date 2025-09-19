produtos = []

for i in range(3):
    produto = {
        "nome" : input(f"Digite o nome do {i + 1}° produto: "),
        "preco": float(input(f'Digite o preço do {i + 1} produto: '))
}
    produtos.append(produto)

print(produtos)

nomePesquisa = input("Pesquise um nome: ")

find = False

for p in produtos:
    if nomePesquisa == p["nome"]:
        find = True
        print(f"Produto: {p["nome"]} | Preço: {p["preco"]}")
        break
    
if find == False:
    print('Produto inexistente')