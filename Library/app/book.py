

class Book:

    def __init__(self, title, authors, pages, release_year, price, category):
        self._title = title
        self._authors = authors
        self._pages = pages
        self._release_year = release_year
        self._price = price
        self._category = category

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, author):
        self._authors.append(author)

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        self._pages = pages

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, release_year):
        self._release_year = release_year

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return f'Book<name: {self._title}>'
