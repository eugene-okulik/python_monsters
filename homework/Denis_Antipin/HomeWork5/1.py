number = 8
while True:
    user_num_is = int(input('Введите цифру '))
    if user_num_is != number:
        print('Попробуй снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
