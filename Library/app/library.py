from typing import List
from .book import Book


class Library:
    _BOOKS: List[Book] = []

    def __init__(self, name: str, address: str):
        self._name = name
        self._address = address

    def get_books_count(self):
        return f'Library have {len(self._BOOKS)} Books'

    def show_books(self):
        for book in self._BOOKS:
            print(repr(book))

    @classmethod
    def add_book(cls, book: Book):
        cls._BOOKS.append(book)

    def __str__(self) -> str:
        return f'Library<name: {self._name}>'


if __name__ == "__main__":
    l = Library('էլեկտրոնային գրադարան', 'Kapan')
    l2 = Library('էլեկտրոնային գրադարան 2', 'Kapan')

    print(l)
    print(l2)

