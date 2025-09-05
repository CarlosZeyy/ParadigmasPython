temp = float(input("Digite o valor da temperatura: "))
umidade = int(input("Digite o valor da umidade: "))

if temp > 25: 
    if umidade > 60 :
        print("Ar quente e úmido")
    elif umidade < 60 :
        print("Ar quente e seco")
else :
    if umidade > 60 :
        print("Ar frio e úmido")
    elif umidade < 60 :
        print("Ar frio e seco")