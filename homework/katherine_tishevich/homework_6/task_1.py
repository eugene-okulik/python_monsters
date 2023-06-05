# Создайте такую программу:
# Пользователь вводит два числа
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2. А если результат изначального
# умножения меньше или равно 20, то он умножается на 3
import operator


def possibility_of_user_numbers(*args):
    sum_user_number = operator.mul(*args)
    if sum_user_number >= 20:
        number_result = sum_user_number * 2
    else:
        number_result = sum_user_number * 3
    print(number_result)


number_sequence = [int(input("Input your number: ")) for _ in range(2)]
possibility_of_user_numbers(*number_sequence)
