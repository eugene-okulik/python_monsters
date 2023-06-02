import random
import utils as l6_utils
from homework.eugene_okulik.lesson_5 import utils as l5_utils
from homework.eugene_okulik.lesson_5 import lesson5
from utils2 import custom_variable_for_example as cvfe


print(random.random() * 1000)
print(random.randint(1, 5))
print(random.randrange(1, 50, 3))
my_list = ['first', 'second', 'third']
print(random.choice(my_list))

a = 1 / 3
print(round(a, 2))

b = -1
c = 1

print(abs(c))
my_list2 = [2, 6, 1]
print(sorted(my_list2, reverse=True))
print(sorted(my_list, reverse=True))
print(sorted(my_list, reverse=True, key=lambda x: len(x)))
# my_list2 = sorted(my_list2)
my_list2.sort(reverse=True)
print(my_list2)

print(max(my_list2))
print(min(my_list2))
print(sum(my_list2))
print(sum(my_list2) / len(my_list2))  # среднее арифметическое

for i, word in enumerate(my_list):
    # print(word)
    print(f'{i}.', word)

i = 0
while i < 10:
    print('hello')
    i += 1

for i in range(10):
    print('hello')

print(list(range(10)))

z = False
x = ''
y = 0
w = []
if z:
    print('Hello')
if x:
    print('Hello')
if y:
    print('Hello')
if w:
    print('Hello')

my_list3 = [1, True, '', {'a': 'b'}]
print(all(my_list3))
print(any(my_list3))


print(l6_utils.my_var)
print(l6_utils.my_func())
print(lesson5.lesson5)
print(cvfe)
