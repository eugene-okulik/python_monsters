my_string = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper '
    'at, dignissim vitae libero!'
)
my_list = my_string.split()
text_with_ing = ''
for word in my_list:
    if word[-1].isalpha() or word[-1].isdigit():
        text_with_ing += f'{word}ing '
    else:
        text_with_ing += f'{word[:-1]}ing{word[-1]} '
print(text_with_ing)


first = 'I'
second = 'Love'
third = 'Python'
print(first + second + third)
