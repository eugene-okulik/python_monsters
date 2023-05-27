# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение
a = float(input("Input number 'a' for operating: "))
b = float(input("Input number 'b' for operating: "))
values_sum = a + b
values_residual = a - b
values_multiplication = a * b
print(f"{values_sum} - sum of numbers;", f"{values_residual} - residual of numbers;"
      f"{values_multiplication} - multiplication of numbers.")
