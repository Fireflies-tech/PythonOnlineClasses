
# a = 5
# print(type(a))
# a = 'str'
# print(type(a))

a: int = 5
s: str = 'ediue'

a = 9
#
# print(a)
#
#
from typing import List, Dict, Any, Union, NewType, Optional, Type


def do_sort(arr: List[int], reverse: Optional[int] = None) -> List[str]:
    return list(map(str, sorted(arr)))


l: List[int] = [11, 56, 5, 6, 96, 612]

print(do_sort(l))


data: Dict[Union[int, str], List] = {
    1: [
        {

        },
        {

        }
    ],
    'name': [
        {

        },
        {

        }
    ]
}


BookId = NewType('BookId', int)
book_id: BookId = BookId(123456)

print(book_id)

# def show_type(pattern: Type[str]):
#     print(pattern)
#
#
# show_type(int)


class Book:
    id = None
    name = None


def show_book_name(b: Book):
    print(b.name)


b = Book()
b1 = Book()

show_book_name(b)

