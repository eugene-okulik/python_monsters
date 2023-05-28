# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте “Etiam tincidunt neque erat, quis
# molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после этого
# выводит получившийся текст на экран.
text_before_modernization = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl," \
                            " facilisis vitae semper at, dignissim vitae libero"
text_after_modernization = ""
for word in text_before_modernization.split():
    if ',' in word:
        symbol_index = word.index(',')
        word = word[:symbol_index] + 'ing' + ', '
        text_after_modernization += word
    elif '.' in word:
        symbol_index = word.index('.')
        word = word[:symbol_index] + 'ing' + '. '
        text_after_modernization += word
    else:
        word += 'ing' + ' '
        text_after_modernization += word
print(f"Check updated text: {text_after_modernization}")
