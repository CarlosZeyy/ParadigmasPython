while True :
    password = str(input("Digite a senha: "))

    if len(password) < 8 :
        print("Senha deve conter 8 caracteres")

    if password == "INFINITY" or password == "infinity":
        print("Você digitou a senha certa!")
        break
    