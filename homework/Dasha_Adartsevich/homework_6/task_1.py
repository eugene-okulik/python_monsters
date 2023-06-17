def multiply(num_1, num_2):
    return num_1 * num_2


number_one = int(input('Enter first number '))
number_two = int(input('Enter second number '))

first_result = multiply(number_one, number_two)

if first_result <= 20:
    new_result = multiply(first_result, 3)
else:
    new_result = multiply(first_result, 2)
print(new_result)


multiply(number_one, number_two)
