def function_for_decorator(func):

    def identifying_operation(num_1, num_2):
        if num_1 == num_2:
            operation = '+'
        if num_1 > num_2:
            operation = '-'
        if num_1 < num_2:
            operation = '/'

    return identifying_operation(first_num, second_num)


first_num = int(input('enter first number '))
second_num = int(input('enter second number '))


@function_for_decorator
def calc(num_1, num_2, operation):
    if operation == '+':
        print(num_1 + num_2)
    if operation == '-':
        print(num_2 - num_1)
    if operation == '/':
        print(num_1 / num_2)


calc(first_num, second_num)
