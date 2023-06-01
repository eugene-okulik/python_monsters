# create dictionary
my_dict = ({'tuple': (2, 10, 3.14, 'name', False), 'list': [10, 'value', 15, 20, 'text'],
            'dict': {1: 'value1', 2: 'value2', 3: 'value3', 4: 'value4', 5: 'value5'},
            'set': {12, 30, 1, 'none', False, 5.98},
            'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
            })
# edit tuple
print(my_dict['tuple'][1:])
# edit list
my_dict['list'].append(123)
my_dict['list'].pop(1)
# edit dict
my_dict['dict'][('I am a tuple',)] = 'my_tuple'
my_dict['dict'].pop(2)
# edit set
my_dict['set'].add('new_element')
my_dict['set'].remove(5.98)
# edit str
print(my_dict['str'][:8])
print(len(my_dict['str']))
print(my_dict['str'][43:43 + 4])
print(my_dict['str'][::3])
print(my_dict['str'].index('pretium'))
print(my_dict['str'].count('l'))
# print my dictionary
print(my_dict)
