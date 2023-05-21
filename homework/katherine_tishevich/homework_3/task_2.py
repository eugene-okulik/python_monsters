# Даны действительные числа x и y. Получить x − y / 1 + xy
x = float(input("Input number of 'x' for operating: "))
y = float(input("Input number of 'y' for operating: "))
result = ((x - 1) / 1) + x * y
print('Result of operation: x − y / 1 + xy with x = {} and y = {} -> {}'.format(x, y, result))
