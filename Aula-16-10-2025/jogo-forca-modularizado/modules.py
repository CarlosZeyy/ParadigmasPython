import os, time

usedLetters = []

def updateUi(tip, wrong, word) :
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*20)
    print('   JOGO DA FORCA')
    print("="*20)
    print(f'\nDica: {tip}')
    print(f'\nTentativas restantes: {3 - wrong}')

    if usedLetters: 
        print(f'Letras que já foram usadas: {" ".join(sorted(usedLetters))}')
        time.sleep(1)

    print(f'\nPalavra: {" ".join(word)}\n')
    char = input('Digite uma letra: ')
    return char.upper()

def checkLetter(wordT, secret, empty):
    if wordT in secret:
        for i in range(len(secret)):
            if secret[i] == wordT:
                empty[i] = wordT

        print(f'Você digitou a letra: {wordT}')
        print('Você acertou a letra!')
        time.sleep(1)
        return True
    else:
        print(f'A letra "{wordT}" não está na palavra.')
        print('Você errou a letra!')
        time.sleep(2)
        return False

def win(empty, word):
    if '_' not in empty:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Parabéns!! Você acertou a palavra: {word}')
        time.sleep(1)
        print('FIM DE JOGO.')
        time.sleep(2)
        return True
    return False

def lose(wrong, word):
    if wrong == 3:
        print('\nVocê zerou todas as suas tentativas!')
        print(f"A palavra secreta era: {word}")
        time.sleep(1)
        print('FIM DE JOGO.')
        time.sleep(2)
        return True
    return False

def quitGame(wordT):
    if wordT == '#':
        print('Finalizando jogo...')
        time.sleep(1)
        return True
    return False
    
def letter(wordT):
        if len(wordT) != 1 or not wordT.isalpha():
            print('Invalido! Digite apenas uma letra.')
            time.sleep(1)
            return True