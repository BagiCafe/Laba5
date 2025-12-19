from src.collections_user import BookCollection, IndexDict
from src.class_book import Book, FictionBook, ComicBook


class TestBookCollection:
    def test_empty_collection(self):
        collection = BookCollection()
        assert len(collection) == 0

    def test_add_one_book(self):
        collection = BookCollection()
        book = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "444")
        collection.append_collection(book)
        assert len(collection) == 1

    def test_add_books(self):
        collection = BookCollection()
        book1 = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "444")
        book2 = Book("Мастер и Маргарита", "Булгаков", 1967, "Роман", "222")
        collection.append_collection(book1)
        collection.append_collection(book2)
        assert len(collection) == 2

    def test_collection_contains(self):
        collection = BookCollection()
        book = Book("Наруто", "Кисимото", 1999, "Сёнен", "333")
        collection.append_collection(book)
        assert book in collection

    def test_collection_not_contains(self):
        collection = BookCollection()
        book1 = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "444")
        book2 = Book("Мастер и Маргарита", "Булгаков", 1967, "Роман", "222")
        collection.append_collection(book1)
        assert book2 not in collection

    def test_get_first_book(self):
        collection = BookCollection()
        book = Book("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Научная фантастика", "000")
        collection.append_collection(book)
        assert collection[0] == book

    def test_iterate_collection(self):
        collection = BookCollection()
        book1 = Book("1984", "Оруэлл", 1949, "Антиутопия", "111")
        book2 = Book("Мастер и Маргарита", "Булгаков", 1967, "Роман", "222")
        collection.append_collection(book1)
        collection.append_collection(book2)
        books = list(collection)
        assert books == [book1, book2]

    def test_remove_book(self):
        collection = BookCollection()
        book = Book("Наруто", "Кисимото", 1999, "Сёнен", "333")
        collection.append_collection(book)
        collection.remove_collection(book)
        assert len(collection) == 0


class TestIndexDict:
    def test_empty_index(self):
        index = IndexDict()
        assert len(index) == 0

    def test_add_to_index(self):
        index = IndexDict()
        book = Book("Бэтмен", "Миллер", 1986, "Супергерои", "555")
        index.append_book(book)
        assert len(index) == 1

    def test_find_isbn(self):
        index = IndexDict()
        book = Book("Программирование на Python", "Лутц", 2013, "Программирование", "666")
        index.append_book(book)
        assert index["666"] == book

    def test_find_author(self):
        index = IndexDict()
        book = Book("1984", "Оруэлл", 1949, "Антиутопия", "111")
        index.append_book(book)
        books = index[("author", "Оруэлл")]
        assert len(books) == 1
        assert book in books

    def test_find_year(self):
        index = IndexDict()
        book = Book("Мастер и Маргарита", "Булгаков", 1967, "Роман", "222")
        index.append_book(book)
        books = index[("year", 1967)]
        assert len(books) == 1
        assert book in books

    def test_check_isbn_index(self):
        index = IndexDict()
        book = Book("Наруто", "Кисимото", 1999, "Сёнен", "333")
        index.append_book(book)
        assert "333" in index

    def test_check_author_index(self):
        index = IndexDict()
        book = Book("Преступление и наказание", "Достоевский", 1866, "Роман", "444")
        index.append_book(book)
        assert ("author", "Достоевский") in index

    def test_check_year_index(self):
        index = IndexDict()
        book = Book("Бэтмен", "Миллер", 1986, "Супергерои", "555")
        index.append_book(book)
        assert ("year", 1986) in index

    def test_remove_from_index(self):
        index = IndexDict()
        book = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "444")
        index.append_book(book)
        index.remove_book(book)
        assert len(index) == 0
        assert "444" not in index