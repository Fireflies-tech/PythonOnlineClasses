from app import Author, Book, Library

from random import randint

from datetime import date


def init_authors(n):
    return [Author(f'Name-{i}', 20+i) for i in range(n)]


def init_books_with_authors(n):
    books = []

    for i in range(n):
        books.append(Book(
            title=f"Title - {i}",
            authors=init_authors(randint(1, 10)),
            pages=randint(100, 10000),
            release_year=date.today(),
            price=randint(3000, 50000),
        ))

    return books


library = Library('էլեկտրոնային գրադարան', 'Kapan')


books = init_books_with_authors(6)

for book in books:
    library.add_book(book)


print(library.get_books_count())


for book in library:
    print(repr(book))

