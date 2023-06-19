# Создайте такую программу:
# Пользователь вводит два числа
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2. А если результат изначального
# умножения меньше или равно 20, то он умножается на 3
import operator


def possibility_of_user_numbers(*numbers):
    """my solutions"""
    multiply_users_number = operator.mul(*numbers)

    def mult_number(*number):
        print(multiply_users_number * number[0])

    if multiply_users_number >= 20:
        mult_number(2)
    else:
        mult_number(3)


number_sequence = [int(input("Input your number: ")) for _ in range(2)]
possibility_of_user_numbers(*number_sequence)


def multiply(x, y):
    """solutions from lesson"""
    return x * y


first_mul = multiply(*number_sequence)
if first_mul > 20:
    result = multiply(first_mul, 2)
else:
    result = multiply(first_mul, 3)
print(result)
