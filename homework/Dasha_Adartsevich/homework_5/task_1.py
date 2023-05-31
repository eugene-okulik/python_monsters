my_string = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, ' \
          'facilisis vitae semper at, dignissim vitae libero'
my_list = my_string.split()
text_with_ing = ''
for word in my_list:
    if ',' in word:
        text_with_ing += word.replace(',', 'ing, ')
    elif '.' in word:
        text_with_ing += word.replace('.', 'ing. ')
    else:
        text_with_ing += f'{word}ing '
print(text_with_ing)
