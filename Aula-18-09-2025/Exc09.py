maiorIdade = []

for i in range(3):
    pessoa = {
        "nome": input(f'Digite o nome da {i + 1}° pessoa: '),
        "idade": int(input(f'Digite a idade da {i + 1}° pessoa: '))
    }
    if (pessoa["idade"]) > 18:
        maiorIdade.append(pessoa)

print(maiorIdade)