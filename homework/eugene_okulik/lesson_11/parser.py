with open('av.txt', 'r') as data_file:
    file_data = data_file.read()


# print(file_data)
file_to_list = file_data.split('\n')
# print(file_to_list)

all_lists = []
category_list = []
for x in file_to_list:
    if x:
        category_list.append(x)
    else:
        all_lists.append(category_list.copy())
        category_list.clear()
all_lists.append(category_list.copy())
category_list.clear()

# print(all_lists)

for categ in all_lists:
    print(f'{categ[0]}: {", ".join(categ[1:])}')
