# Создайте класс book с атрибутами:
#
# материал страниц, наличие текста, название книги, автор, кол-во страниц, ISBN,
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг. # После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага

# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников. # После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

class Book:
    material_pages = "Paper"
    presence_of_text = True

    def __init__(self, book_title, author, count_of_pages, isbn, reserved=False):
        self.book_title = book_title
        self.author = author
        self.count_of_pages = count_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def print_details(self):
        if self.reserved:
            print(
                f"Название: {self.book_title}, Автор: {self.author}, Кол-во страниц: {self.count_of_pages}, "
                f"Материал страниц: {self.material_pages}, зарезервирована")
        else:
            print(
                f"Название: {self.book_title}, Автор: {self.author}, Кол-во страниц: {self.count_of_pages}, "
                f"Материал страниц: {self.material_pages}")


book1 = Book('Война и мир', 'Толстой', 798, 1234567890123, False)
book2 = Book("Идиот", "Достоевкий", 1265, 1234446440123, False)
book3 = Book("Красная шапочка", "Перро", 69, 5664567890123, False)
book4 = Book("451 градус по Фаренгейту", "Бредбери", 1028, 1463566390123, False)
book5 = Book("Вечера на хуторе...", "Гоголь", 956, 1635345340123, True)

book5.reserved = True

book1.print_details()
book2.print_details()
book3.print_details()
book4.print_details()
book5.print_details()


class SchoolBook(Book):

    def __init__(self, book_title, author, count_of_pages, isbn, subject, grade, hometasks, reserved=False):
        super().__init__(book_title, author, count_of_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.hometasks = hometasks

    def print_details(self):
        if self.reserved:
            print(
                f"Название: {self.book_title}, Автор: {self.author}, cтраниц: {self.count_of_pages}, "
                f"предмет: {self.subject}, класс: {self.grade}, зарезервирована")
        else:
            print(
                f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.count_of_pages}, "
                f"предмет: {self.subject}, класс: {self.grade}")


school_book1 = SchoolBook('Алгебра', 'Рябцев', 325, 123121233122, "Математика", 5, True)
school_book2 = SchoolBook('Русский язык', 'Воронков', 250, 123124343129, "Русский язык", 8, True)
school_book3 = SchoolBook('Рисование', 'Кузнецов', 60, 12312123355, "ИЗО", 3, False)
school_book4 = SchoolBook('Золотой век', 'Иванов', 555, 123121233127, "Литература", 10, True)
school_book5 = SchoolBook('Геометрия', 'Колокольчиков', 75, 123121233128, "Математика", 7, True)

school_book3.reserved = True

school_book1.print_details()
school_book2.print_details()
school_book3.print_details()
school_book4.print_details()
school_book5.print_details()
