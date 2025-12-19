from src.class_book import Book, FictionBook, ComicBook


class TestBook:
    def test_create_book(self):
        book = Book("Мёртвые души", "Николай Гоголь", 1842, "Поэма", "002")
        assert book.title == "Мёртвые души"

    def test_book_author(self):
        book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "222")
        assert book.author == "Михаил Булгаков"

    def test_book_year(self):
        book = Book("Наруто", "Кисимото", 1999, "Сёнен", "333")
        assert book.year == 1999

    def test_book_genre(self):
        book = Book("Программирование на Python", "Марк Лутц", 2013, "Программирование", "666")
        assert book.genre == "Программирование"

    def test_book_isbn(self):
        book = Book("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Научная фантастика", "000")
        assert book.isbn == "000"

    def test_book_repr(self):
        book = Book("Война и мир", "Лев Толстой", 1869, "Исторический роман", "111")
        rep = repr(book)
        assert "Война и мир" in rep
        assert "Лев Толстой" in rep


class TestFictionBook:
    def test_create_fictionbook(self):
        fbook = FictionBook("Преступление и наказание", "Достоевский", 1866, "Роман", "444", 672)
        assert fbook.pages == 672

    def test_fictionbook_is_book(self):
        fbook = FictionBook("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "444", 223)
        assert isinstance(fbook, Book)

    def test_fictionbook_repr(self):
        fbook = FictionBook("Братья Карамазовы", "Фёдор Достоевский", 1880, "Философский роман", "001", 796)
        rep = repr(fbook)
        assert "796 стр." in rep


class TestComicBook:
    def test_create_comicbook(self):
        comic = ComicBook("Ходячие мертвецы", "Роберт Киркман", 2003, "Хоррор", "555", "графический роман")
        assert comic.comic_type == "графический роман"

    def test_comicbook_is_book(self):
        comic = ComicBook("Человек-паук: Удивительная фантазия", "Стэн Ли", 1962, "Супергерои", "777", "комикс")
        assert isinstance(comic, Book)

    def test_comicbook_repr(self):
        comic = ComicBook("Клинок, рассекающий демонов", "Койохару Готогэ", 2016, "Сёнен", "888", "манга")
        rep = repr(comic)
        assert "манга" in rep