class BookCollection:
    """
    Пользовательская списковая коллекция книг
    """
    def __init__(self):
        self.books = []

    def __iter__(self):
        return iter(self.books)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        """Обеспечивает доступ к книгам по индексу или срезу"""
        spicok = self.books[key]
        if isinstance(spicok, list):
            return BookCollection(spicok)
        return spicok

    def __contains__(self, book):
        """Проверяем содержится ли книга в коллекции"""
        return book in self.books

    def append_collection(self, book):
        """Добавляет книгу в коллекцию"""
        self.books.append(book)

    def remove_collection(self, book):
        """Удаляет книгу из коллекции"""
        if book in self.books:
            self.books.remove(book)


class IndexDict:
    """
    Пользовательская словарная коллекция для индексации книг по ISBN, автору и году
    """
    def __init__(self):
        self.isbn = {}
        self.author = {}
        self.year = {}

    def __iter__(self):
        return iter(self.isbn.values())

    def __len__(self):
        return len(self.isbn)

    def __getitem__(self, key):
        """
        Доступ к книгам по различным ключам:
        - Если ключ str (ISBN)
        - Если ключ tuple ("author", имя)
        - Если ключ tuple ("year", год)
        """
        if isinstance(key, str):
            return self.isbn[key]
        elif isinstance(key, tuple) and len(key) == 2:
            index, value = key
            if index == "author":
                return self.author.get(value, [])
            elif index == "year":
                return self.year.get(value, [])
        raise KeyError(f"Kлюч: {key} не найден")

    def __contains__(self, key):
        """Проверяет наличие ключа в индексах"""
        if isinstance(key, str):
            return key in self.isbn
        elif isinstance(key, tuple) and len(key) == 2:
            index, value = key
            if index == "author":
                return value in self.author
            elif index == "year":
                return value in self.year
        return False

    def append_book(self, book):
        """Добавляем книгу во все индексы"""
        if book.isbn in self.isbn:
            return
        self.isbn[book.isbn] = book

        if book.author not in self.author:
            self.author[book.author] = []
        if book not in self.author[book.author]:
            self.author[book.author].append(book)

        if book.year not in self.year:
            self.year[book.year] = []
        if book not in self.year[book.year]:
            self.year[book.year].append(book)

    def remove_book(self, book):
        """Удаляем книгу из всех индексов"""
        if book.isbn in self.isbn:
            del self.isbn[book.isbn]

        if book.author in self.author and book in self.author[book.author]:
            self.author[book.author].remove(book)
            if not self.author[book.author]:
                del self.author[book.author]

        if book.year in self.year and book in self.year[book.year]:
            self.year[book.year].remove(book)
            if not self.year[book.year]:
                del self.year[book.year]