# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'
import random


def bonus_for_salary(salary, bonus):
    if bonus:
        remuneration = salary + bonus
        print(f"{salary}, {bonus} - '${remuneration}'")


bonus_for_salary(salary=int(input("Input salary: ")), bonus=random.choice([True, False]))  # bool(random.random())
