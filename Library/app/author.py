
from .person import Person


class Author(Person):

    def __init__(self, name, age, address=None, books=None):
        super().__init__(name, age, address)
        self._books = books or []

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, book):
        self._books.append(book)

    def __str__(self):
        return f'Author<name: {self._name}>'
