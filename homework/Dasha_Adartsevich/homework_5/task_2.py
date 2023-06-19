a = 7
while True:
    b = int(input('Enter any number! '))
    if b == a:
        print('Congratulations, you guessed!')
        break
    elif b != a:
        print('Sorry, try again!')
