def products(x):
    yield x
    print('one more')
    print('Thats all')

print(list(products(1)))

