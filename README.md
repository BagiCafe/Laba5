# LABA5 ( Отладĸа ĸодовой базы проеĸта на Python с помощью средств отладĸи)

## Ошибки

### Ошибка 1 - Ошибка границы цикла (off-by-one)
Место : ```main.py```, метод ```find_author```

Симптом:

При поиске книг по автору программа выдает ```IndexError```

Как воспроизвести:

Запустить симуляцию с seed=0 и шагом=10.

Отладка:

Установлен breakpoint на  цикле: ```for i in range(len(found_books) + 1) ```

Причина:

Цикл выполняется на одну итерацию больше, чем нужно

Исправление:

Убрать в цикле + 1 ( ```for i in range(len(found_books))``` )

Доказательства:

<img width="1920" height="1080" alt="debug_1" src="https://github.com/user-attachments/assets/7bb9a7c1-dbfc-4449-9051-062c75604ec3" />

<img width="1838" height="735" alt="bug_1" src="https://github.com/user-attachments/assets/62d325e4-2b69-48d2-878b-65b0efbd534b" />


### Ошибка 2 - Перехват слишком общего исключения
Место : ```main.py```, метод ```main()```

Симптом:

При вводе некорректного seed программа скрывает детали ошибки

Как воспроизвести:

Запустить симуляцию с seed=www и шагом=10.

Отладка:

Установлен breakpoint на : ```except Exception as e ```

Причина:

Использование ```Exception``` вместо конкретного ```ValueError```

Исправление:

Использовать ```ValueError``` (```except ValueError```)

Доказательства:

<img width="1920" height="1080" alt="Ошибка_дебагер_2" src="https://github.com/user-attachments/assets/76795007-e93c-4102-a868-e16445089125" />

Ошибки в командной строке нет


### Ошибка 3 - Сравнение через is вместо ==
Место : ```main.py```, метод ```main()```

Симптом:

При вводе строки "None" программа не распознаёт этот случай

Как воспроизвести:

Запустить симуляцию с seed=None и шагом=10.

Отладка:

Установлен breakpoint на условие: ```elif seed is "None"```

Причина:

```is``` сравнивает идентичность объектов в памяти

Исправление:

Изменить ```is``` на ```==``` (```elif seed == "None"``` )

Доказательства:

<img width="1920" height="1080" alt="Ошибка_дебагер_3" src="https://github.com/user-attachments/assets/4b1811af-a292-4b97-a7aa-f8d777534e39" />

<img width="1841" height="405" alt="Ошибка_3" src="https://github.com/user-attachments/assets/571923b9-785a-4341-9fb5-8d1f13e707a9" />


### Ошибка 4 - Перепутанные аргументы или поля объекта
Место : ```src/class_book.py```, класс ```Library``` и метод ```__init__```

Симптом:

При создании библиотеки и попытке добавить книгу программа выдает ```AttributeError```

Как воспроизвести:

Запустить симуляцию с seed=7 и шагом=10.

Отладка:

Установлен breakpoint на : ```self.name = BookCollection()``` и ```self.books = name```

Причина:

Неправильная инициализация полей объекта

Исправление:

Поменять местами ```name``` и ```BookCollection()``` (```self.name``` = ```name``` и ```self.books``` = ```BookCollection()```)

Доказательства:

<img width="1920" height="1080" alt="Ошибка_дебагер_4" src="https://github.com/user-attachments/assets/0cbbc3a5-4f9a-480e-8ec8-690c8bb06b5e" />

<img width="1836" height="729" alt="Ошибка_4" src="https://github.com/user-attachments/assets/6d14d322-3c23-4b62-b9a4-9636b90f0ddd" />


### Ошибка 5 - Неправильный разбор строки или входных данных
Место : ```main.py```, метод ```add_book```

Симптом:

При добавлении книги программа выдвет ```ValueError```

Как воспроизвести:

Запустить симуляцию с seed=1 и шагом=10.

Отладка:

Установлен breakpoint на : ```books_pool.remove(str(book))```

Причина:

Попытка удалить строковое представление объекта из списка, содержащего объекты

Исправление:

Не использовать ```str``` (```books_pool.remove(book)```)

Доказательства:

<img width="1920" height="1080" alt="Ошибка_дебагер_5" src="https://github.com/user-attachments/assets/844101e5-da9e-4f9b-95c5-f64d3f55ea02" />

<img width="1834" height="705" alt="Ошибка_5" src="https://github.com/user-attachments/assets/42c2fd6d-3da9-41d4-9287-82cdca8d6750" />
