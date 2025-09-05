temp = float(input("Digite o valor da temperatura: "))
umidade = int(input("Digite o valor da umidade: "))

if temp > 25 and umidade > 60 :
    print("Ar quente e úmido")
elif temp > 25 and umidade < 60 :
    print("Ar quente e seco")
elif temp <= 25 and umidade > 60 :
    print("Ar frio e úmido")
elif temp <= 25 and umidade < 60 :
    print("Ar frio e seco")