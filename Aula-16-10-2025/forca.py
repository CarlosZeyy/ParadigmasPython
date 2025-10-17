import random, os, time

wrongs = 0
words = ['PYTHON', 'JAVA', 'KOTLIN', 'JAVASCRIPT', 'TYPESCRIPT']
tips = [
    'É uma serpente e uma linguagem', 
    'Linguagem robusta referência em aplicações de back-end', 
    'Linguagem criada pela JetBrains e usada para desenvolvimento mobile Android', 
    'Linguagem padrão para web front-end', 
    'Um superconjunto do JavaScript'
]

randIndex = random.randint(0, len(words) - 1)
secretWord = words[randIndex]
randTip = tips[randIndex]

emptyWord = ['_' for word in secretWord]

def updateUi() :
    os.system('clear')
    print('Jogo da forca')
    print(f'Dica: {randTip}')
    print(f'Tentativas restantes: {3 - wrongs}')
    print(emptyWord)
    char = input('Digite uma letra: ').upper()
    return char


while wrongs < 3 and '_' in emptyWord:
    wordTyped = updateUi()

    if wordTyped == '#':
        print('Finalizando jogo...')
        break

    if wordTyped in secretWord:
        for i in range(len(secretWord)):
            if secretWord[i] == wordTyped:
                emptyWord[i] = wordTyped

        print(f'Você digitou a letra: {wordTyped}')
        print('Acertou!')
    else:
        wrongs += 1
        print(f'Você digitou a letra: {wordTyped}')
        print('Errou!')
        time.sleep(2)

    if wrongs == 3:
        print('Você zerou todas as suas tentativas!')
        print('Finalizando jogo...')
        time.sleep(2)
    
    if '_' not in emptyWord:
        os.system('clear')
        print(f'Parabéns!! Você acertou a palavra: {secretWord}')
        time.sleep(2)