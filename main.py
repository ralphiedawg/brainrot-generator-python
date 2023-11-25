import random as rand
import time
# Stupid Gen Alpha Vocab List
vocab = ['skibidi', 'fanum tax', 'grimace shake', 'ohio', 'rizz', 'gyatt', 'kai cenat', 'sigma']
vocabIndex = 0

def question():
    userInput = input('Warning: Are you sure about this? yes/no: ')
    userInput = userInput.lower()
    match userInput:
        case 'yes':
            while True:
                vocabIndex = rand.randint(0,7)
                print(vocab[vocabIndex])
                time.sleep(0.3)
        case 'no':
            print('Probably better for your sanity that you said no.')
        case _:
            print("Let's try this again")
            print("Yes or No, please.")
            question()
question()