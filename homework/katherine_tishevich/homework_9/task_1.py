# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из первого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение
def calc_note(func):
    """Decorator"""
    def wrapper(first_number, second_number):
        if first_number == second_number:
            result = func(first_number, second_number, operation='+')
            return result
        elif first_number > second_number:
            result = func(first_number, second_number, operation='-')
            return result
        elif second_number > first_number:
            result = func(first_number, second_number, operation='/')
            return result
        elif first_number or second_number < 0:
            result = func(first_number, second_number, operation='*')
            return result
    return wrapper


@calc_note
def calc(first_number, second_number, operation):
    if operation == '+':
        print('Answer:', first_number + second_number)
    elif operation == '-':
        print('Answer:', first_number - second_number)
    elif operation == '/':
        print('Answer:', first_number / second_number)
    elif operation == '*':
        print('Answer:', first_number * second_number)


calc(first_number=int(input("Input your first number: ")), second_number=int(input("Input your second number: ")))
