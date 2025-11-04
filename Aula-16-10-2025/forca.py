import random, os, time

wrongs = 0
usedLetters = []
words = ['PYTHON', 'JAVA', 'KOTLIN', 'JAVASCRIPT', 'TYPESCRIPT', 'HTML', 'CSS', 'REACT', 'ANGULAR', 'VUE']
tips = [
    'É uma serpente e uma linguagem.', 
    'Linguagem robusta referência em aplicações de back-end.', 
    'Linguagem criada pela JetBrains e usada para desenvolvimento mobile Android.', 
    'Linguagem padrão para web front-end.', 
    'Um superconjunto do JavaScript que adiciona tipagem estática.',
    'Linguagem de marcação para criar páginas web.',
    'Usado para estilizar elementos escritos em uma linguagem de marcação.',
    'Biblioteca JavaScript para criar interfaces de usuário.',
    'Framework de aplicação web baseado em TypeScript.',
    'Framework JavaScript progressivo para construir interfaces de usuário.'
]

randIndex = random.randint(0, len(words) - 1)
secretWord = words[randIndex]
secretTip = tips[randIndex]

emptyWord = ['_' for word in secretWord]

def updateUi() :
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*20)
    print('   JOGO DA FORCA')
    print("="*20)
    print(f'\nDica: {secretTip}')
    print(f'\nTentativas restantes: {3 - wrongs}')

    if usedLetters:
        print(f'Letras que já foram usadas: {" ".join(sorted(usedLetters))}')

    print(f'\nPalavra: {" ".join(emptyWord)}\n')
    char = input('Digite uma letra: ')
    return char.upper()

while wrongs < 3 and '_' in emptyWord:
    letterTyped = updateUi()

    if letterTyped == '#':
        print('Finalizando jogo...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    if len(letterTyped) != 1 or not letterTyped.isalpha():
        print('Invalido! Digite apenas uma letra.')
        time.sleep(1)
        continue

    if letterTyped in usedLetters:
        print(f'\nA letra "{letterTyped}" já foi usada. Tente outra')
        time.sleep(2)
        continue

    usedLetters.append(letterTyped)

    if letterTyped in secretWord:
        for i in range(len(secretWord)):
            if secretWord[i] == letterTyped:
                emptyWord[i] = letterTyped

        print(f'Você digitou a letra: {letterTyped}')
        print('Você acertou a letra!')
        time.sleep(1)
    else:
        wrongs += 1
        print(f'A letra "{letterTyped}" não está na palavra.')
        print('Você errou a letra!')
        time.sleep(2)

    if wrongs == 3:
        print('Você zerou todas as suas tentativas!')
        print(f"A palavra secreta era: {secretWord}")
        time.sleep(1)
        print('FIM DE JOGO.')
        time.sleep(2)
    
    if '_' not in emptyWord:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Parabéns!! Você acertou a palavra: {secretWord}')
        time.sleep(1)
        print('FIM DE JOGO.')
        time.sleep(2)