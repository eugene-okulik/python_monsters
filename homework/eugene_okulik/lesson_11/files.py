import os
import json
import _io

path_to_dir = os.path.dirname(os.path.dirname(__file__))
# /home/eugene/projects/python_monsters/homework/eugene_okulik/lesson_11
# C:\users\eugene\projects\python_monsters\homework\eugene_okulik\lesson_11

# path_to_file = path_to_dir + '/' + 'data1.txt'
# path_to_file = path_to_dir + '\\' + 'data1.txt'
path_to_file = os.path.join(path_to_dir, 'data2.txt')
print(path_to_file)

text = 'John\'s'

my_file = open(path_to_file)
print(json.load(my_file))
my_file.close()

with open(path_to_file) as my_file:
    print(json.load(my_file))

print(open(path_to_file))
