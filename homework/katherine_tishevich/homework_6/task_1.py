# Создайте такую программу:
# Пользователь вводит два числа
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2. А если результат изначального
# умножения меньше или равно 20, то он умножается на 3
import operator


def possibility_of_user_numbers(*args):
    multiply_users_number = operator.mul(*args)

    def multiply_by_two(multiply_users_number):
        print(multiply_users_number * 2)

    def multiply_by_three(multiply_users_number):
        print(multiply_users_number * 3)

    if multiply_users_number >= 20:
        multiply_by_two(multiply_users_number)
    else:
        multiply_by_three(multiply_users_number)


number_sequence = [int(input("Input your number: ")) for _ in range(2)]
possibility_of_user_numbers(*number_sequence)