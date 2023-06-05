import random

salary = int(input('Enter salary '))
bonus = [True, False]
bonus_1 = random.choice(bonus)
bonus_2 = round(random.random() * 1000)


def result(x, y, z):
    if y:
        print(f'{x}, {y} - {x + z}$')
    else:
        print(f'{x}, {y} - {x}$')


print(result(salary, bonus_1, bonus_2))
