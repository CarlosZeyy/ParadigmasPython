def _main(pacientes, chave, operacao, desc_valor):
    valor_principal = operacao(paciente[chave] for paciente in pacientes)

    print(f"Pacientes com {desc_valor}: ")

    for paciente in pacientes:
        if paciente[chave] == valor_principal:
            print(f"Nome: {paciente["nome"]}, {chave.upper()}: {paciente[chave]:.2f}")

def maior_imc(pacientes):
    _main(pacientes, "imc", max, "Maior IMC")

def maior_tmb(pacientes):
    _main(pacientes, "tmb", max, "Maior TMB")

def menor_imc(pacientes):
    _main(pacientes, "imc", min, "Menor IMC")

def menor_tmb(pacientes):
    _main(pacientes, "tmb", min, "Menor TMB")

def mostrar_dados(pacientes):
    print("\n--- Informações de todos os pacientes registrados ---")
    for paciente in pacientes:
        print(f"Nome: {paciente["nome"]} | Idade: {paciente['idade']} | Sexo: {paciente['sexo']} | Peso: {paciente['peso']} | Altura: {paciente['altura']} | IMC: {paciente['imc']:.2f} | TMB: {paciente['tmb']:.2f}\n")