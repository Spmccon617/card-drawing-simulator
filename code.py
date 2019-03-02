from random import randint

while True:
    card = randint(1,52)
    drawCard = input('Do you want to draw a card?')
    
    if drawCard is 'yes':
        print(card)
    else:
        print('Nevermind')
        break
    
    drawAgain = input('Do you want to draw again?')
    
    if drawAgain is 'yes':
        print(card)
    else:
        break
