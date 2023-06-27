import os
import datetime


path_to_homework_directory = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_to_file = os.path.join('eugene_okulik', 'hw_11_file', 'data.txt')
path_to_file_1 = os.path.join(path_to_homework_directory, path_to_file)

with open(path_to_file_1, 'r') as my_file:
    file_data = my_file.readlines()

for line in file_data:
    if line == file_data[0]:
        date_1 = f'{line.split()[1]} {line.split()[2]}'
    if line == file_data[1]:
        date_2 = f'{line.split()[1]} {line.split()[2]}'
    if line == file_data[2]:
        date_3 = f'{line.split()[1]} {line.split()[2]}'


# 1. 2022-05-14 20:34:13.212967 - распечатать эту дату, но на три года позже
first_date = datetime.datetime.fromisoformat(date_1)
first_date_in_three_years = first_date + datetime.timedelta(days=1096)
print(first_date_in_three_years)


# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
second_date = datetime.datetime.fromisoformat(date_2)
print(second_date.strftime('%A'))


# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата
third_date = datetime.datetime.fromisoformat(date_3)
now = datetime.datetime.now()
days_ago = now - third_date
print(f'{days_ago.days} дней назад')
