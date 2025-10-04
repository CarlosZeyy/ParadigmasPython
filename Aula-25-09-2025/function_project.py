def maior_imc(pacientes):
    valor_maior_imc = pacientes[0]["imc"]

    for paciente in pacientes:
        if paciente["imc"] > valor_maior_imc:
            valor_maior_imc = paciente["imc"]

    print("Paciente com o maior IMC: ")

    for paciente in pacientes:
        if paciente["imc"] == valor_maior_imc:
            print(f"Nome: {paciente["nome"]}, IMC: {paciente["imc"]:.2f}")

def maior_tmb(pacientes):
    valor_maior_tmb = pacientes[0]["tmb"]

    for paciente in pacientes:
        if paciente["tmb"] > valor_maior_tmb:
            valor_maior_tmb = paciente["tmb"]

    print("Paciente com o maior TMB: ")

    for paciente in pacientes:
        if paciente["tmb"] == valor_maior_tmb:
            print(f"Nome: {paciente["nome"]}, TMB: {paciente["tmb"]:.2f}")

def menor_imc(pacientes):
    valor_menor_imc = pacientes[0]["imc"]

    for paciente in pacientes:
        if paciente["imc"] < valor_menor_imc:
            valor_menor_imc = paciente["imc"]
    
    print("Paciente com o menor IMC: ")

    for paciente in pacientes:
        if paciente["imc"] == valor_menor_imc:
            print(f"Nome: {paciente["nome"]}, IMC: {paciente["imc"]:.2f}")

def menor_tmb(pacientes):
    valor_menor_tmb = pacientes[0]["tmb"]

    for paciente in pacientes:
        if paciente["tmb"] < valor_menor_tmb:
            valor_menor_tmb = paciente["tmb"]
        
    print("Paciente com o menor TMB: ")

    for paciente in pacientes:
        if paciente["tmb"] == valor_menor_tmb:
            print(f"Nome: {paciente["nome"]}, TMB: {paciente["tmb"]:.2f}")

def mostrar_dados(pacientes):
    for paciente in pacientes:
        print(f"Nome: {paciente["nome"]} | Idade: {paciente['idade']} | Sexo: {paciente['sexo']} | Peso: {paciente['peso']} | Altura: {paciente['altura']} | IMC: {paciente['imc']:.2f} | TMB: {paciente['tmb']:.2f}\n")
