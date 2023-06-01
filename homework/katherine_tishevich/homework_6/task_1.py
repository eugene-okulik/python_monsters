# Создайте такую программу:
# Пользователь вводит два числа
# Программа умножает одно число на другое.
# Если результат этого умножения больше 20, то этот результат умножается на 2. А если результат изначального
# умножения меньше или равно 20, то он умножается на 3
def possibility_of_user_numbers(first_number, second_number):
    sum_user_number = first_number * second_number
    if sum_user_number >= 20:
        user_number_more_then_twenty = sum_user_number * 2
        print(f"Result = {user_number_more_then_twenty}")
    else:
        user_number_less_then_twenty = sum_user_number * 3
        print(f"Result = {user_number_less_then_twenty}")


possibility_of_user_numbers(first_number=float(input("Input your first number: ")),
                            second_number=float(input("Input your second number: ")))
