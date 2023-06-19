# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
# 32, 30, 28, 24, 23]
# С помощью функции map создайте из этого списка новый список с жаркими днями. Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру и самую низкую.
def mapply(temperature):
    if temperature > 28:
        return temperature


def mapping_hot_day(temperatures):
    mapping_day = list(map(mapply, temperatures))  # нужно использовать filter для создания нового списка вместо map
    mapping_day = [t for t in mapping_day if t]
    print(f"New list - {mapping_day}, max number - {max(temperatures)}, min number {min(temperatures)}")


mapping_hot_day(temperatures=[20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31,
                              33, 31, 30, 32, 30, 28, 24, 23])
