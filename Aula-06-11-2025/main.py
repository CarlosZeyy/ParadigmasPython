from bingo import SorteadorBingo as sorteador
import os, time

while True:

    print("="*40)
    print("                 BINGO")
    print("="*40)

    qtd_numeros_bingo = int(input('Digite a quantidade de números do bingo: '))
    meu_bingo = sorteador(qtd_numeros_bingo)

    jogo_rodando = True

    while jogo_rodando:
        print('\nMenu de opções:\n')
        print('1 - Sortear novo número\n'
              '2 - Sair\n')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            meu_bingo.sortear_numero()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            print(f'Ultima bolinha sorteada: {meu_bingo.ultimo_numero_sorteado}\n')
            print(f'Bolinhas sorteadas ({meu_bingo.bolinhas_sorteadas}): {meu_bingo.bolinhas_sorteadas}')

            if meu_bingo.todos_numeros_sorteados:
                jogo_rodando = False
                print('O BINGO ACABOU')
                time.sleep(2)
                os.system('cls' if os.name == "nt" else 'clear')

        elif opcao == 2:
            print('BINGO FINALIZADO')
            time.sleep(2)
            os.system('cls' if os.name == "nt" else 'clear')
            jogo_rodando = False
            break

        else: 
            print('Opção inválida! Digite 1 ou 2.')
            time.sleep(2)
            os.system('cls' if os.name == "nt" else 'clear')
            print(f'Ultima bolinha sorteada: {meu_bingo.ultimo_numero_sorteado}\n')
            print(f'Bolinhas sorteadas ({meu_bingo.bolinhas_sorteadas}): {meu_bingo.bolinhas_sorteadas}')
        
    if opcao == 2:
        print('BINGO FINALIZADO')
        time.sleep(2)
        os.system('cls' if os.name == "nt" else 'clear')
        break