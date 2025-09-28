pacientes = []

for i in range(3):
    paciente = {
        "nome": input("Digite o seu nome: "),
        "idade": int(input("Digite sua idade: ")),
        "sexo": input("Digite o seu sexo (F/M):  "),
        "peso": float(input("Digite o seu peso: ")),
        "altura": float(input("Digite a sua altura (Metros): ")),
    }
    imcCalculado = paciente["peso"] / (paciente["altura"] ** 2)
    paciente["imc"] = imcCalculado

    if paciente["sexo"] == "F" or paciente["sexo"] == "f":
        tmbM = 9.99 * paciente["peso"] + 6.25 * (paciente["altura"] * 100) - 4.92 * paciente["idade"] - 161
        paciente["tmb"] = tmbM
    elif paciente["sexo"] == "M" or paciente["sexo"] == "m":
        tmbH = 9.99 * paciente["peso"] + 6.25 * (paciente["altura"] * 100) - 4.92 * paciente["idade"] + 5
        paciente["tmb"] = tmbH
    else:
        print("Erro ao receber dados, verifique se os campos foram preenchidos corretamente.")
        break
    pacientes.append(paciente)


print("Opções: ")
print("1 - Maior IMC")
print("2 - Maior TMB")
print("3 - Menor IMC")
print("4 - Menor TMB")
print("5 - Exibe as informações dos usuarios registrados\n")
opcoes = int(input("Escolha uma das opções: "))

if opcoes == 1:
    valor_maior_imc = pacientes[0]["imc"]

    for paciente in pacientes:
        if paciente["imc"] > valor_maior_imc:
            valor_maior_imc = paciente["imc"]

    print("Paciente com o maior IMC: ")

    for paciente in pacientes:
        if paciente["imc"] == valor_maior_imc:
            print(f"Nome: {paciente["nome"]}, IMC: {paciente["imc"]:.2f}")

elif opcoes == 2:
    valor_maior_tmb = pacientes[0]["tmb"]

    for paciente in pacientes:
        if paciente["tmb"] > valor_maior_tmb:
            valor_maior_tmb = paciente["tmb"]

    print("Paciente com o maior TMB: ")

    for paciente in pacientes:
        if paciente["tmb"] == valor_maior_tmb:
            print(f"Nome: {paciente["nome"]}, TMB: {paciente["tmb"]:.2f}")

elif opcoes == 3:
    valor_menor_imc = pacientes[0]["imc"]

    for paciente in pacientes:
        if paciente["imc"] < valor_menor_imc:
            valor_menor_imc = paciente["imc"]
    
    print("Paciente com o menor IMC: ")

    for paciente in pacientes:
        if paciente["imc"] == valor_menor_imc:
            print(f"Nome: {paciente["nome"]}, IMC: {paciente["imc"]:.2f}")

elif opcoes == 4:
    valor_menor_tmb = pacientes[0]["tmb"]

    for paciente in pacientes:
        if paciente["tmb"] < valor_menor_tmb:
            valor_menor_tmb = paciente["tmb"]
        
    print("Paciente com o menor TMB: ")

    for paciente in pacientes:
        if paciente["tmb"] == valor_menor_tmb:
            print(f"Nome: {paciente["nome"]}, TMB: {paciente["tmb"]:.2f}")

elif opcoes == 5:
    for paciente in pacientes:
        print(f"Nome: {paciente["nome"]} | Idade: {paciente['idade']} | Sexo: {paciente['sexo']} | Peso: {paciente['peso']} | Altura: {paciente['altura']} | IMC: {paciente['imc']:.2f} | TMB: {paciente['tmb']:.2f}\n")