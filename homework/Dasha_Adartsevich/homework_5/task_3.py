a = 0
while True:
    a += 1
    if a % 3 == 0 and a % 5 == 0:
        print('FuzzBuzz')
    elif a % 3 == 0:
        print('Fuzz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print(a)
    if a > 99:
        break
