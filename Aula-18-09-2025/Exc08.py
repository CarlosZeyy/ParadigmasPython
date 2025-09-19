for i in range(3):
    produto = {
        "nome" : input(f"Digite o nome do {i + 1}° produto: "),
        "preco": float(input(f'Digite o preço do {i + 1} produto: '))
}

nomePesquisa = input("Pesquise um nome: ")

if nomePesquisa != produto["nome"]:
    print('Produto inexistente')
else: 
    print(produto["nome"])