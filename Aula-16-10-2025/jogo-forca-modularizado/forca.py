import random, time, modules as uiModule, words_tips as wt

wrongs = 0
words = wt.words
tips = wt.tips
equalLetters = uiModule.usedLetters

randIndex = random.randint(0, len(words) - 1)
secretWord = words[randIndex]
secretTip = tips[randIndex]

emptyWord = ['_' for word in secretWord]

while wrongs < 3 and '_' in emptyWord:
    letterTyped = uiModule.updateUi(secretTip, wrongs, emptyWord)

    if uiModule.quitGame(letterTyped):
        break

    if uiModule.letter(letterTyped):
        continue

    if letterTyped in equalLetters:
        print(f'\nA letra "{letterTyped}" já foi usada. Tente outra')
        time.sleep(2)
        continue

    equalLetters.append(letterTyped)

    if not uiModule.checkLetter(letterTyped, secretWord, emptyWord):
        wrongs += 1

    if uiModule.lose(wrongs, secretWord):
        break
    
    if uiModule.win(emptyWord, secretWord):
        break