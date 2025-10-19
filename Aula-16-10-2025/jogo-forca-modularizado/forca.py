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
    wordTyped = uiModule.updateUi(secretTip, wrongs, emptyWord)

    if uiModule.quitGame(wordTyped):
        break

    if uiModule.letter(wordTyped):
        continue

    if wordTyped in equalLetters:
        print(f'\nA letra "{wordTyped}" já foi usada. Tente outra')
        time.sleep(2)
        continue

    equalLetters.append(wordTyped)

    if not uiModule.checkLetter(wordTyped, secretWord, emptyWord):
        wrongs += 1

    if uiModule.lose(wrongs, secretWord):
        break
    
    if uiModule.win(emptyWord, secretWord):
        break