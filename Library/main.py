from app import Author, Book, Library


def init_authors(n):
    return [Author(f'Name-{i}', 20+i) for i in range(n)]


authors = init_authors(10)


print(authors)

