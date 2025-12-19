class Book:
    """
    Базовый класс, который показывает книгу в библиотеке

    Args:
        title: Название книги
        author: Автор книги
        year: Год издания
        genre: Жанр книги
        isbn: ISBN книги
    """
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        return f'Book("{self.title}", {self.author}, {self.year}, "{self.genre}", ISBN: {self.isbn})'


class FictionBook(Book):
    """
    Художественная книга (рассказ, роман, повесть)

    Args:
        title: Название книги
        author: Автор книги
        year: Год издания
        genre: Жанр книги
        isbn: ISBN книги
        pages: Количество страниц
    """
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, pages: int):
        super().__init__(title, author, year, genre, isbn)
        self.pages = pages

    def __repr__(self) -> str:
        return f'FictionBook("{self.title}", {self.pages} стр.)'


class ComicBook(Book):
    """
    Комикс (американские комикс, манга, графический роман)

    Args:
        title: Название комикса
        author: Автор комикса
        year: Год издания
        genre: Жанр комикса
        isbn: ISBN комикса
        comic_type: Вид комикса
    """
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, comic_type: str):
        super().__init__(title, author, year, genre, isbn)
        self.comic_type = comic_type

    def __repr__(self) -> str:
        return f'ComicBook("{self.title}", вид: {self.comic_type})'