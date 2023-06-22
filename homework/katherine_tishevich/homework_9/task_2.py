# Дан такой кусок прайс листа:
# (Копируйте эту переменную (константу) в код прямо как есть)
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи генераторов превратите этот текст в словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)
import re


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def lict_compr_task(value):
    numbers_list = re.findall(r'\d+', value)
    numbers_list = list(map(int, numbers_list))
    letters_list = re.findall(r'\b[а-яА-Я]\w+', value)
    price_dictionary = {key: value for key, value in zip(letters_list, numbers_list)}
    print(price_dictionary)


lict_compr_task(value=PRICE_LIST)
