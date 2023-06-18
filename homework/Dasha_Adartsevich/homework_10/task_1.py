# First class
class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, name, author, number_of_pages, isbn, reservation):
        self.name = name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reservation = reservation

    def is_reserved(self):
        return self.reservation

    def __str__(self):
        if self.is_reserved():
            return f'Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, материал: ' \
                   f'{self.page_material}, зарезервирована'
        return f'Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, материал: ' \
               f'{self.page_material}'


book_1 = Book(name='Мастер и Маргарита', author='Булгаков', number_of_pages=500, isbn=456, reservation=False)
book_2 = Book(name='Повелитель мух', author='Голдинг', number_of_pages=250, isbn=478, reservation=False)
book_3 = Book(name='Мартин Иден',author='Лондон', number_of_pages=354, isbn=67895, reservation=False)
book_4 = Book(name='Грозовой перевал', author='Бронте', number_of_pages=645, isbn=10908, reservation=False)
book_5 = Book(name='Убить пересмешника', author='Харпер Ли', number_of_pages=284, isbn=4569087, reservation=True)

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)


# Second Class
class SchoolBook(Book):
    tasks = True

    def __init__(self, name, author, number_of_pages, isbn, reservation, subject, year):
        super().__init__(name, author, number_of_pages, isbn, reservation)
        self.subject = subject
        self.year = year

    def __str__(self):
        if self.is_reserved():
            return f'Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, предмет: '\
                   f'{self.subject}, класс: {self.year}, зарезервирована'
        return f'Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, предмет: ' \
               f'{self.subject}, класс: {self.year}'


book_6 = SchoolBook(name='Алгебра', author='Иванов', number_of_pages=390, isbn=56748, reservation=False,
                    subject='Математика', year=9)
book_7 = SchoolBook(name='История', author='Петров', number_of_pages=270, isbn=7893, reservation=False,
                    subject='История', year=10)
book_8 = SchoolBook(name='География', author='Николаев', number_of_pages=234, isbn=234, reservation=True,
                    subject='География', year=11)


print(book_6)
print(book_7)
print(book_8)
