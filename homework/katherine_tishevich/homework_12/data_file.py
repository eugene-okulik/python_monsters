# Нужно прочитать файлик, который лежит в моих папках. Здесь: python_monsters/homework/eugene_okulik/hw_11_file/data.txt
#
# Файлик не копируйте и никуда не переносите. Прочитайте его питоном, найдите в нём даты и сделайте с ними то, что
# после этих дат написано. Опирайтесь на то, что структура каждой строки одинакова: сначала идет номер, потом дата,
# потом дефис и после него текст
import os
import datetime


data_list = []


path_to_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_to_file = path_to_dir + '/eugene_okulik/hw_11_file/data.txt'
with open(f'{path_to_file}', 'r') as data_file:
    for line in data_file:
        new_line = line.split()
        next_line = new_line[1] + ' ' + new_line[2]
        data_list.append(next_line)

first_date = data_list[0].replace('2022', '2025')
second_date = (datetime.datetime.fromisoformat(data_list[1].split()[0])).strftime('%A')
third_date = (datetime.date.fromisoformat(data_list[2].split()[0]) - datetime.date.today()).days
print(first_date, '\n', second_date, '\n', third_date)
