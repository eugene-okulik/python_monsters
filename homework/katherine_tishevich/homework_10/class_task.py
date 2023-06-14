# Библиотека
# Первый класс
# Создайте класс book с атрибутами:
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9
class Book:
    page_material = 'бумага'
    text_on_page = True

    def __init__(self, book_name, author, page_count, isbn, reserve):
        self.book_name = book_name
        self.author = author
        self.page_count = page_count
        self.ISBN = isbn
        self.reserve = reserve


first_book = Book(book_name='python_1', author='author_for_python_1', page_count=100, isbn='00000001',
                  reserve=False)
second_book = Book(book_name='python_2', author='author_for_python_2', page_count=200, isbn='00000002',
                   reserve=False)
third_book = Book(book_name='python_3', author='author_for_python_3', page_count=300, isbn='00000003',
                  reserve=False)
fourth_book = Book(book_name='python_4', author='author_for_python_4', page_count=400, isbn='00000004',
                   reserve=False)
fifth_book = Book(book_name='python_5', author='author_for_python_5', page_count=500, isbn='00000005',
                  reserve=True)
list_data = [first_book.__dict__,
             second_book.__dict__,
             third_book.__dict__,
             fourth_book.__dict__,
             fifth_book.__dict__]
key = "reserve"
value = True
dict_with_true_conditions = next((d for d in list_data if d.get(key) == value), None)
del dict_with_true_conditions["ISBN"]
del dict_with_true_conditions["reserve"]
dict_with_true_conditions.update({"page_material": Book.__dict__.get("page_material")})
ideal_keys = ["Название", "Автор", "страниц", "материал"]
dict_values = dict_with_true_conditions.values()
new_dict = {ideal_keys: dict_values for ideal_keys, dict_values in zip(ideal_keys, dict_values)}
update_format = []
for key, item in new_dict.items():
    update_format.append("{}: {}".format(key, item))
result_books = ", ".join(update_format)
print(result_books)


class SchoolBooks(Book):
    subject = 'Information Technology'
    level = 9
    tasks_in_book = True


first_lesson_book = SchoolBooks(book_name="Music", author="Rohmaninov", page_count=100, isbn='12323239',
                                reserve=False)
second_lesson_book = SchoolBooks(book_name="History", author="Napoleon", page_count=1, isbn='000000000',
                                 reserve=False)
third_lesson_book = SchoolBooks(book_name="OOP", author="Оле Джохан Дал и Кристен Нюгорт", page_count=100000,
                                isbn='100000000', reserve=True)


list_data = [first_lesson_book.__dict__,
             second_lesson_book.__dict__,
             third_lesson_book.__dict__]
key = "reserve"
value = True
dict_with_true_conditions_school_books = next((d for d in list_data if d.get(key) == value), None)
del dict_with_true_conditions_school_books["ISBN"]
del dict_with_true_conditions_school_books["reserve"]
dict_with_true_conditions_school_books.update({"subject": SchoolBooks.__dict__.get("subject")})
dict_with_true_conditions_school_books.update({"level": SchoolBooks.__dict__.get("level")})
ideal_keys = ["Название", "Автор", "страниц", "предмет", "класс"]
dict_values = dict_with_true_conditions_school_books.values()
new_dict = {ideal_keys: dict_values for ideal_keys, dict_values in zip(ideal_keys, dict_values)}
update_format = []
for key, item in new_dict.items():
    update_format.append("{}: {}".format(key, item))
result_school_books = ", ".join(update_format)
print(result_school_books)
