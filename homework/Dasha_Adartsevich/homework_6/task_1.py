def multiply(num_1, num_2):
    result = num_1 * num_2
    if result <= 20:
        new_result = result * 3
    else:
        new_result = result * 2
    return new_result


number_one = int(input('Enter first number '))
number_two = int(input('Enter second number '))

print(multiply(number_one, number_two))
