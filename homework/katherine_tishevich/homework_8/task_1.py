# Попросите пользователя ввести дату и попробуйте преобразовать дату в формат питона.
# В случае, если пользователь не угадал с форматом ввода даты, вы получите исключение.
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату.
import datetime


def data_func():
    try:
        validate_date_format = datetime.datetime.strptime(user_data, "%d-%m-%Y %H:%M:%S.%f")
        validate_date_format.strftime("%d-%m-%Y %H:%M:%S.%f")
    except ValueError:
        print("Input your data in format dd-mm-yyyy h:m:s.f")


user_data = input("Input your data: ")
data_func()
