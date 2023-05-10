
class Library:
    _BOOKS = []

    def __init__(self, name, address):
        self._name = name
        self._address = address

    @classmethod
    def add_book(cls, book):
        cls._BOOKS.append(book)

    def __str__(self):
        return f'Library<name: {self._name}>'


if __name__ == "__main__":
    l = Library('էլեկտրոնային գրադարան', 'Kapan')
    l2 = Library('էլեկտրոնային գրադարան 2', 'Kapan')

    print(l)
    print(l2)

