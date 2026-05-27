# qa_python

В классе TestBooksCollector() реализованы следующие тесты:
- test_add_new_book_add_two_books. Пример теста из пре-кода. Проверка работы метода add_new_book класса BooksCollector для кейса добавления двух книг.   
- test_add_new_book_incorrect_name. Проверка работы метода add_new_book класса BooksCollector для двух кейсов с некорректными названиями книг (длина названия 0 и длина названия > 40 символов).
- test_set_book_genre_existing_genre. Проверка работы метода set_book_genre класса BooksCollector для кейса сохранения жанра для одной книги.
- test_get_book_genre_existing_book. Проверка работы метода get_book_genre класса BooksCollector для кейса одной книги, существующей в словаре books_genre. 
- test_get_books_with_specific_genre_horrors. Проверка работы метода get_books_with_specific_genre класса BooksCollector для кейса двух книг жанра 'Ужасы'.
- test_get_books_genre_one_book. Проверка работы метода get_books_genre класса BooksCollector для кейса получения жанра одной книги.
- test_get_books_for_children_one_book. Проверка работы метода get_books_for_children класса BooksCollector: проверка, что метод не возвращает книги жанров 'Ужасы' и 'Детективы'.
- test_add_book_in_favorites_add_one_book. Проверка работы метода add_book_in_favorites класса BooksCollector для кейса добавления одной книги в избранное.
- test_delete_book_from_favorites_one_book. Проверка работы метода delete_book_from_favorites класса BooksCollector для кейса удаления одной книги из избранного.
- test_get_list_of_favorites_books_two_books. Проверка работы метода get_list_of_favorites_books класса BooksCollector для кейса получения списка избранного из двух книг.
    
В каждом тесте создаётся отдельный экземпляр класса BooksCollector(). Это реализовано с помощью фикстуры, сохранённой в файле conftest.py.