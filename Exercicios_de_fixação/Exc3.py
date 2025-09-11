while True :
    password = input("Digite a senha: ")
    # password = password.upper()

    if len(password) != 7 :
        print("Senha deve conter 7 caracteres")

    if password == "ESTACIO" :
        print("Você digitou a senha certa!")
        break
    else :
        print("Senha errada! digite a senha novamente!")
    