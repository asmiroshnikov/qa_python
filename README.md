# qa_python
from main import BooksCollector
class TestBooksCollector:
def test_add_new_book():
    collector = BooksCollector()
    collector.add_new_book("Book1")
    assert "Book1" in collector.get_books_genre()

from main import BooksCollector
class TestBooksCollector:
def test_set_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Book2")
    collector.set_book_genre("Book2", "Фантастика")
    assert collector.get_book_genre("Book2") == "Фантастика"

from main import BooksCollector
class TestBooksCollector:
def test_get_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Book3")
    assert collector.get_book_genre("Book3") == ""

from main import BooksCollector
class TestBooksCollector:
def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book("AdventureBook")
    collector.set_book_genre("AdventureBook", "Фэнтези")
    assert collector.get_books_with_specific_genre("Фэнтези") == ["AdventureBook"]

from main import BooksCollector
class TestBooksCollector:
def test_get_books_genre():
    collector = BooksCollector()
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    assert collector.get_books_genre() == {"Book1": "", "Book2": ""}

from main import BooksCollector
class TestBooksCollector:
def test_getbooks_for_children():
    collector = BooksCollector()
    collector.addnewbook("ChildrenBook1")
    collector.addnewbook("AdultBook")
    collector.setbookgenre("ChildrenBook1", "Детективы")
    assert "AdultBook" not in collector.getbooksforchildren()

from main import BooksCollector
class TestBooksCollector:
def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.addnewbook("MyFavoriteBook")
    collector.addbookinfavorites("MyFavoriteBook")
    assert collector.getlistoffavoritesbooks() == ["MyFavoriteBook"]

from main import BooksCollector
class TestBooksCollector:
def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book("BookToRemoveFromFavorites")
    collector.add_book_in_favorites("BookToRemoveFromFavorites")
    collector.delete_book_from_favorites("BookToRemoveFromFavorites")
    assert collector.get_list_of_favorites_books() == []

from main import BooksCollector
class TestBooksCollector:
def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book("Favorite1")
    collector.add_new_book("Favorite2")
    collector.add_book_in_favorites("Favorite1")
    collector.add_book_in_favorites("Favorite2")
    assert len(collector.get_list_of_favorites_books()) == 2
