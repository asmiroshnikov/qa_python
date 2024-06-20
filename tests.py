from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        assert "Book1" in collector.get_books_genre()


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book2")
        collector.set_book_genre("Book2", "Фантастика")
        assert collector.get_book_genre("Book2") == "Фантастика"


    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book3")
        assert collector.get_book_genre("Book3") == ""


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("AdventureBook")
        collector.set_book_genre("AdventureBook", "Фэнтези")
        assert collector.get_books_with_specific_genre("Фэнтези") == ["AdventureBook"]


    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_new_book("Book2")
        assert collector.get_books_genre() == {"Book1": "", "Book2": ""}


    def test_getbooks_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("ChildrenBook1")
        collector.add_new_book("AdultBook")
        collector.set_book_genre("ChildrenBook1", "Детективы")
        assert "AdultBook" not in collector.get_books_for_children()


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("MyFavoriteBook")
        collector.add_book_in_favorites("MyFavoriteBook")
        assert collector.get_list_of_favorites_books() == ["MyFavoriteBook"]


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("BookToRemoveFromFavorites")
        collector.add_book_in_favorites("BookToRemoveFromFavorites")
        collector.delete_book_from_favorites("BookToRemoveFromFavorites")
        assert collector.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Favorite1")
        collector.add_new_book("Favorite2")
        collector.add_book_in_favorites("Favorite1")
        collector.add_book_in_favorites("Favorite2")
        assert len(collector.get_list_of_favorites_books()) == 2
