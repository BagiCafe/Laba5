import random
from src.class_book import Book, FictionBook, ComicBook
from src.class_library import Library

def creating_library():
    """Создаем библиотеку с книгами"""
    library = Library()
    adding_books = [
        FictionBook("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Научная фантастика", "000", 158),
        FictionBook("Война и мир", "Лев Толстой", 1869, "Исторический роман", "111", 1225),
        FictionBook("Преступление и наказание", "Фёдор Достоевский", 1866, "Психологический роман", "222",672),
        FictionBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "333", 480),
        FictionBook("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "444", 223),
        ComicBook("Ходячие мертвецы", "Роберт Киркман", 2003, "Хоррор", "555", "графический роман"),
        ComicBook("Наруто Книга 1", "Масаси Кисимото", 1999, "Сёнен", "666", "манга"),
        ComicBook("Человек-паук: Удивительная фантазия", "Стэн Ли", 1962, "Супергерои", "777", "комикс"),
        ComicBook("Клинок, рассекающий демонов", "Койохару Готогэ", 2016, "Сёнен", "888", "манга"),
        ComicBook("Люди Икс", "Стэн Ли", 1963, "Супергерои", "999", "комикс")
    ]
    for book in adding_books:
        library.append_book(book)
    return library

def creating_books():
    """Создаем книги"""
    return [
        FictionBook("Братья Карамазовы", "Фёдор Достоевский", 1880, "Философский роман", "001", 796),
        FictionBook("Мёртвые души", "Николай Гоголь", 1842, "Поэма", "002", 464),
        FictionBook("Три мушкетёра", "Александр Дюма", 1844, "Исторический роман", "003", 704),
        ComicBook("Человек-бензопила", "Тацуки Фудзимото", 2018, "Сёнен", "004", "манга"),
        ComicBook("Мстители", "Стэн Ли", 1963, "Супергерои", "005", "комикс"),
        ComicBook("Наруто Книга 2", "Масаси Кисимото", 1999, "Сёнен", "006", "манга")
    ]

def add_book(library, books_pool):
    """Добавляем случайную книгу"""
    if not books_pool:
        print("  Нет доступных книг для добавления")
        return

    book = random.choice(books_pool)
    print(f"  Добавляем: {book}")
    library.append_book(book)
    # №5 Ошибка неправильный разбор строки или входных данных. Удаляем строку вместо объекта
    books_pool.remove(str(book))
    print(f"  Успешно добавлено")

def remove_book(library, books_pool):
    """Удаляем случайную книгу"""
    if len(library.books) > 0:
        books_list = list(library.books)
        index = random.randint(0, len(books_list) - 1)
        book = books_list[index]
        print(f"  Удаляем: {book}")
        library.remove_book(book)
        books_pool.append(book)
        print(f"  Успешно удалено")
    else:
        print("  Библиотека пуста")

def find_author(library, books_pool=None):
    """Ищем книги по автору"""
    authors = ["Рэй Брэдбери", "Лев Толстой", "Фёдор Достоевский", "Михаил Булгаков", "Джоан Роулинг", "Роберт Киркман", "Масаси Кисимото", "Стэн Ли", "Койохару Готогэ"]
    author = random.choice(authors)
    print(f"  Ищем автора: {author}")
    try:
        found_books = library.index[("author", author)]
        print(f"  Найдено: {len(found_books)} книг")
        if found_books:
            # №1 Ошибка границы цикла (off-by-one). Цикл выполняется на одну итерацию больше, чем нужно
            for i in range(len(found_books) + 1):
                book = found_books[i]
                print(f"    {i+1}. {book}")
    except KeyError:
        print(f"  Найдено: 0 книг")

def find_year(library, books_pool=None):
    """Ищем книги по году"""
    year = random.randint(1700, 2025)
    print(f"  Ищем год: {year}")
    try:
        found_books = library.index[("year", year)]
        print(f"  Найдено: {len(found_books)} книг")
        if found_books:
            for i in range(len(found_books)):
                book = found_books[i]
                print(f"    {i+1}. {book}")
    except KeyError:
        print(f"  Найдено: 0 книг")

def find_genre(library, books_pool=None):
    """Ищем книги по жанру"""
    genres = ["Научная фантастика", "Исторический роман", "Сёнен", "Роман", "Фэнтези", "Супергерои", "Сатира"]
    genre = random.choice(genres)
    print(f"  Ищем жанр: {genre}")

    found_books = []
    for book in library.books:
        if hasattr(book, 'genre') and book.genre == genre:
            found_books.append(book)
    print(f"  Найдено: {len(found_books)} книг")
    try:
        if found_books:
            for i in range(len(found_books)):
                book = found_books[i]
                print(f"    {i+1}. {book}")
    except KeyError:
        print(f"  Найдено: 0 книг")

def update_index(library, books_pool=None):
    """Обновляем индекс"""
    print("  Обновление индекса...")

    books_count = len(library.books)
    index_count = len(library.index)

    print(f"  Книг в библиотеке: {books_count}")
    print(f"  Книг в индексе: {index_count}")

    if books_count == index_count:
        print("  Индекс синхронизирован")
    else:
        print("  Расхождение! Индекс требует обновления")

        # Создаем временный новый индекс
        temporary_index = {}
        for book in library.books:
            temporary_index[book.isbn] = book

        # Проверяем какие книги отсутствуют в индексе
        missing = []
        for book in library.books:
            try:
                library.index[book.isbn]
            except KeyError:
                missing.append(book.isbn)

        if missing:
            print(f"  В индексе отсутствуют: {missing}")
        else:
            print("  Все книги присутствуют в индексе")

def find_nonexistent(library, books_pool=None):
    """Ищем несуществующую книгу"""
    print("  Ищем несуществующую книгу...")

    print("  Тест 1: Несуществующий ISBN ")
    try:
        book = library.index["www"]
        print(f"    ОШИБКА: книга - {book} найдена")
    except KeyError:
        print("    Книга не найдена")

    print("  Тест 2: Несуществующий автор")
    try:
        found = library.index[("author", "www")]
        if found:
            print(f"    ОШИБКА: найдено {len(found)} книг")
        else:
            print("    Книги не найдены")
    except KeyError:
        print("    Книги не найдены")

    print("  Тест 3: Несуществующий год")
    try:
        found = library.index[("year", 5000)]
        if found:
            print(f"    ОШИБКА: найдено {len(found)} книг")
        else:
            print("    Книги не найдены")
    except KeyError:
        print("    Книги не найдены")

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """Запускаем симуляцию"""
    if seed is not None:
        random.seed(seed)

    library = creating_library()
    books_pool = creating_books()

    events = [
        ("Добавить книгу", add_book),
        ("Удалить книгу", remove_book),
        ("Найти по автору", find_author),
        ("Найти по году", find_year),
        ("Найти по жанру", find_genre),
        ("Обновить индекс", update_index),
        ("Найти несуществующую книгу", find_nonexistent),
    ]

    print("-" * 40)
    print(f"ПСЕВДОСЛУЧАЙНАЯ СИМУЛЯЦИЯ БИБЛИОТЕКИ")
    print("-" * 40)

    for step in range(1, steps + 1):
        print(f"\nШаг {step}:")
        name, func = random.choice(events)
        print(f"  Событие: {name}")
        func(library, books_pool)

def main():
    print(f"Параметры симуляции")
    steps = int(input("Количество шагов: "))
    seed = input("Seed (Enter для случайного): ")

    if seed == "":
        seed = None
    # №3 Ошибка сравнение через is вместо ==. Условие со строкой None не выполнится
    elif seed is "None":
        print("Неверный формат seed, если хотели использовть None, то используйте Enter")
        seed = input("Seed (Enter для случайного): ")
    else:
        try:
            seed = int(seed)
        # №2 Ошибка перехват слишĸом общего исĸлючения. Использование Exception вместо конкретного ValueError
        except Exception as e:
            print("Неверный формат seed, используется случайный")
            seed = None

    run_simulation(steps=steps, seed=seed)

if __name__ == "__main__":
    main()