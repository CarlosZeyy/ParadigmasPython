from bingo import SorteadorBingo as sorteador
import os, time, opcoes

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

        try:
            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                opcoes.sortear_novo_numero(meu_bingo)
                if meu_bingo.todos_numeros_sorteados:
                    jogo_rodando = False
                
            elif opcao == 2:
                opcoes.sair_bingo()
                jogo_rodando = False
                break

            else:
                print('Opção Inválida! Digite 1 ou 2.')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Ultima bolinha sorteada: {meu_bingo.ultimo_numero_sorteado}\n')
                print(f'Bolinhas sorteadas ({meu_bingo.bolinhas_sorteadas}): {meu_bingo.bolinhas_sorteadas}')

        except ValueError:
            print('\n!!! ERRO: Por favor, digite apenas NÚMEROS (1 ou 2). !!!')
            time.sleep(2)
            os.system('cls' if os.name == "nt" else 'clear')
            continue

    if opcao == 2:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        break