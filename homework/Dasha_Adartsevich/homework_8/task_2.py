import datetime

while True:
    date = input('Enter the date ')
    try:
        python_date = datetime.datetime.strptime(date, '%d-%m-%Y')
        print(python_date)
    except ValueError:
        print('Incorrect date format. Please, use format: dd-mm-yyyy, e.g: 01-08-2014')
