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
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
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

    def check_reserve_book(self):
        return self.reserve

    def __str__(self):
        if self.check_reserve_book():
            return f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.page_count}, материал: ' \
                   f'{self.page_material}, зарезервирована'
        return f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.page_count}, материал: ' \
               f'{self.page_material}'


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
books = [first_book, second_book, third_book, fourth_book, fifth_book]
for book in books:
    print(book)


class SchoolBooks(Book):
    subject = 'Information Technology'
    level = 9
    tasks_in_book = True

    def __str__(self):
        if self.check_reserve_book():
            return f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.page_count}, предмет: ' \
                   f'{self.subject}, класс: {self.level}, зарезервирована'
        return f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.page_count}, предмет: ' \
               f'{self.subject}, класс: {self.level}'


first_lesson_book = SchoolBooks(book_name="Music", author="Rohmaninov", page_count=100, isbn='12323239',
                                reserve=False)
second_lesson_book = SchoolBooks(book_name="History", author="Napoleon", page_count=1, isbn='000000000',
                                 reserve=False)
third_lesson_book = SchoolBooks(book_name="OOP", author="Оле Джохан Дал и Кристен Нюгорт", page_count=100000,
                                isbn='100000000', reserve=True)
school_books = [first_lesson_book, second_lesson_book, third_lesson_book]
for book in school_books:
    print(book)
