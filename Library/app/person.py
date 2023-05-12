from typing import Optional


class Person:

    def __init__(self, name: str, age: int, address: Optional[str] = None):
        self._name = name
        self._age = age
        self._address = address

