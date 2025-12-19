from src.class_library import Library
from src.class_book import Book, FictionBook, ComicBook


class TestLibrary:
    def test_create_library(self):
        library = Library("библиотека")
        assert library.name == "библиотека"

    def test_empty_library(self):
        library = Library()
        assert len(library.books) == 0

    def test_add_fiction_library(self):
        library = Library()
        fbook = FictionBook("Мастер и Маргарита", "Булгаков", 1967, "Роман", "222", 480)
        library.append_book(fbook)
        assert len(library.books) == 1

    def test_add_comic_library(self):
        library = Library()
        comic = ComicBook("Наруто", "Кисимото", 1999, "Сёнен", "333", "манга")
        library.append_book(comic)
        assert len(library.books) == 1

    def test_book_in_library(self):
        library = Library()
        book = Book("Наруто", "Кисимото", 1999, "Сёнен", "333")
        library.append_book(book)
        assert book in library.books

    def test_remove_fiction_library(self):
        library = Library()
        fbook = FictionBook("Преступление и наказание", "Достоевский", 1866, "Роман", "444", 672)
        library.append_book(fbook)
        library.remove_book(fbook)
        assert len(library.books) == 0

    def test_library_repr(self):
        library = Library("библиотека")
        book = Book("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Научная фантастика", "000")
        library.append_book(book)
        rep = repr(library)
        assert "библиотека" in rep

    def test_find_book_index(self):
        library = Library()
        book = Book("Война и мир", "Лев Толстой", 1869, "Исторический роман", "111")
        library.append_book(book)
        assert library.index["111"] == book

    def test_books_in_library(self):
        library = Library()
        book = Book("Клинок, рассекающий демонов", "Койохару Готогэ", 2016, "Сёнен", "888")
        fbook = FictionBook("Люди Икс", "Стэн Ли", 1963, "Супергерои", "999", 100)
        comic = ComicBook("Братья Карамазовы", "Фёдор Достоевский", 1880, "Философский роман", "001", "книга")
        library.append_book(book)
        library.append_book(fbook)
        library.append_book(comic)
        assert len(library.books) == 3