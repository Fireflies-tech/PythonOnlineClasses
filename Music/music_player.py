import datetime
import uuid
from typing import List, Iterable

from pathlib import Path


class Person:
    STORE_PATH = Path('./data/person.txt')

    def __init__(self, full_name: str, age: int, email: str, country: str, password: str = None):
        self.full_name = full_name
        self.age = age
        self.email = email
        self.country = country
        self.password = password or self.generate_password()

        self.__changed = False

    def save(self):
        Path('./data').mkdir(exist_ok=True)
        with open(Person.STORE_PATH, 'a') as pf:
            pf.writelines(f'{self.__dict__}\n')

    @staticmethod
    def get(email):
        with open(Person.STORE_PATH, 'r') as pf:
            line = pf.readline()
            while line:
                if email in line:
                    return Person(**eval(line))
                line = pf.readline()

    def edit(self, auto_save=False, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
                self.__changed = True

        if auto_save:
            self.save()

    @classmethod
    def load(cls) -> Iterable['Person']:
        with open(cls.STORE_PATH, 'r') as pf:
            line = pf.readline()
            while line:
                yield cls(**eval(line))
                line = pf.readline()

    def __str__(self):
        return f'{self.full_name} - {self.email}'

    def __repr__(self):
        return f'Person<{self.full_name}, {self.email}>'

    @staticmethod
    def generate_password():
        return str(uuid.uuid4())


class Artist:
    def __init__(self, full_name: str, avatar_url: str, country: str):
        self.full_name = full_name
        self.avatar_url = avatar_url
        self.country = country


class Song:

    def __init__(self, name: str, artists: List[Artist], genre: str, duration: float):
        self.id = uuid.uuid4()
        self.name = name
        self.artists = artists
        self.genre = genre
        self.duration = duration


class Playlist:
    def __init__(self, title: str, songs: List[Song], created_by: Person):
        self.title: str = title
        self.songs: List = songs
        self.created_by = created_by
        self.created_at = datetime.datetime.now()


if __name__ == '__main__':
    # person1 = Person('Gohar Petrosyan', 26, 'gohar.petrosyan@mail.ru', 'Armenia')
    # person1.save()
    # print(person1)

    # p1 = Person.get('hamazasp.frangulyan17@mail.ru')
    # print(p1)
    # # p2 = Person.get('gohar.petrosyan@mail.ru')
    # # print(p2)
    #
    # p1.edit(
    #     auto_save=True,
    #     full_name='Hamo Frangulyan',
    #     country='Russia',
    # )
    #
    # print(p1, p1.country)

    persons = list(Person.load())

    print(persons)


