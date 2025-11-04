from bingo import SorteadorBingo as sorteador
import os, time

def sortear_novo_numero(bingo):
    bingo.sortear_numero()
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print(f'Ultima bolinha sorteada: {bingo.ultimo_numero_sorteado}\n')
    print(f'Bolinhas sorteadas ({bingo.bolinhas_sorteadas}): {bingo.bolinhas_sorteadas}')

    if bingo.todos_numeros_sorteados == True:
        print('O BINGO ACABOU')
        time.sleep(2)
        os.system('cls' if os.name == "nt" else 'clear')
        return False

def sair_bingo():
    print('BINGO FINALIZADO')
    time.sleep(2)
    os.system('cls' if os.name == "nt" else 'clear')
    return False
