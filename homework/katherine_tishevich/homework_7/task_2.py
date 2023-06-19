# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов, минимальное,
# сумму всех рандомов и их среднее арифметическое.
import random
import statistics


def numbers_magic(data):
    data_storage = []
    while len(data_storage) < 15:
        data_storage.append(data)
    print(f"Minimal number from numbers: {min(data_storage)}, sum of numbers: {sum(data_storage)}, "
          f"arithmetical mean of numbers: {statistics.mean(data_storage)}")


numbers_magic(data=random.random())
