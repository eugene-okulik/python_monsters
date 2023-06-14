PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_from_string = PRICE_LIST.split()
price_list_keys = list(element for element in list_from_string[::2])
price_list_values = list(int(f'{element[:-1]}') for element in list_from_string if element.endswith('р'))
new_dict = {k: v for k, v in zip(price_list_keys, price_list_values)}
print(new_dict)




