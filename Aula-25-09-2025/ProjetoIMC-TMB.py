import function_project as functionPacients

pacientes = []
qtd_pacientes = int(input("Digite a quantidade de pacientes que serão registrados: "))

for i in range(qtd_pacientes):
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

opcoes_disponiveis = {
    1: functionPacients.maior_imc,
    2: functionPacients.maior_tmb,
    3: functionPacients.menor_imc,
    4: functionPacients.menor_tmb,
    5: functionPacients.mostrar_dados,
}

opcao_escolhida = opcoes_disponiveis.get(opcoes)

if opcao_escolhida:
    opcao_escolhida(pacientes)
else:
    print('Opção invalida!')