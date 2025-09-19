numero = int(input('Digite um numero: '))

if numero < 0:
    print('Negativo')
elif (numero % 2 == 0) > 0 or numero == 0 :
    print('Par')
else: 
    print('Impar')
    