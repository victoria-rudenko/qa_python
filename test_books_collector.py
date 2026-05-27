import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book_name', ['Секрет древнего шифра: Загадка утраченной карты', ''])
    def test_add_new_book_incorrect_name(self, book_name, collector):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_existing_genre(self, collector):
        collector.add_new_book('Анна Карамелькина')
        collector.set_book_genre('Анна Карамелькина', 'Комедии')
        assert collector.books_genre['Анна Карамелькина'] == 'Комедии'

    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book('Гарри Поттер и забытый пароль')
        collector.set_book_genre('Гарри Поттер и забытый пароль', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и забытый пароль') == 'Фантастика'

    def test_get_books_with_specific_genre_horrors(self, collector):
        collector.add_new_book('Молчание котов')
        collector.add_new_book('Дракула: чесночные истории')
        collector.add_new_book('Восточный экспресс. Путеводитель')
        collector.set_book_genre('Молчание котов', 'Ужасы')
        collector.set_book_genre('Дракула: чесночные истории', 'Ужасы')
        collector.set_book_genre('Восточный экспресс. Путеводитель', 'Детективы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_existing_genre(self, collector):
        collector.add_new_book('Гуси-Лебеди')
        collector.set_book_genre('Гуси-Лебеди', 'Мультфильмы')
        assert collector.get_books_genre()['Гуси-Лебеди'] == 'Мультфильмы'

    @pytest.mark.parametrize('adult_genre,children_genre',
                             [['Ужасы', 'Фантастика'], ['Детективы', 'Мультфильмы'], ['Ужасы', 'Комедии']])
    def test_get_books_for_children_one_book(self, adult_genre, children_genre, collector):
        collector.add_new_book('Колобок')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Колобок', children_genre)
        collector.set_book_genre('Сияние', adult_genre)
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_new_book(self, collector):
        collector.add_new_book('Репка')
        collector.add_book_in_favorites('Репка')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_one_book(self, collector):
        collector.add_new_book('Виммельбух')
        collector.add_new_book('Словарь')
        collector.add_book_in_favorites('Виммельбух')
        collector.add_book_in_favorites('Словарь')
        collector.delete_book_from_favorites('Словарь')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_two_books(self, collector):
        collector.add_new_book('1984')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('Дюна')
        assert len(collector.get_list_of_favorites_books()) == len(collector.favorites)
