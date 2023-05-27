# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
from math import sqrt


first_leg = float(input("Input first value for first leg: "))
second_leg = float(input("Input second value for operating second leg: "))
hypotenuse = sqrt(first_leg**2 + second_leg**2)
perimeter = hypotenuse + first_leg + second_leg
print(f"Hypotenuse = {hypotenuse}, perimetr = {perimeter}")
