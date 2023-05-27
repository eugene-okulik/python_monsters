# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.
from math import sqrt


first_value = float(input("Input first number for operating: "))
second_value = float(input("Input second number for operating: "))
value_arithmetical_mean = (first_value + second_value) / 2
value_geometric_mean = sqrt(first_value * second_value)
print('Arithmetical mean = {}, geometric mean = {}'.format(value_arithmetical_mean, value_geometric_mean))
