def function_for_decorator(func):
    def wrapper():
        def compare_numbers(number_1, number_2):
            if number_1 == number_2:
                operation = '+'
            if number_1 > number_2:
                operation = '-'
            if number_2 > number_1:
                operation = '/'
            if number_1 < 0 or number_2 < 0:
                operation = '*'
            return func(first, second, operation)
        return compare_numbers
    return wrapper()


@function_for_decorator
def calc(first, second, operation):
    if operation == '+':
        result = first + second
    if operation == '-':
        result = second - first
    if operation == '/':
        result = first / second
    if operation == '*':
        result = first * second
    return result


first = int(input('Enter first number '))
second = int(input('Enter second number '))
print(calc(first, second))
