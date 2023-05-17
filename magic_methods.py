from typing import List


class Point(object):
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def __add__(self, other) -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other) -> bool:
        # return self.x == other.x and self.y == other.y
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'[{self.x}, {self.y}]'


# point1 = Point(12, 10)
# point2 = Point(12, 10)
#
# print(point1)
# print(point2)
#
# # print(hash(point1))
# # print(hash(point2))
# point3 = point2 + point1
#
# # print(point3)
#
# print(point1 == point2)
#
#
# print((12, 10) == (12, 10))
#
#
# d = {
#     point1: 'Point 1',
#     point2: 'Point 2',
#     1: 'Point 1',
#     1: 'Point 10',
# }
#
# print(d)


class A:

    def __init__(self, title):
        self.title = title
        self._a = 5
        self.__k = 5

    def __del__(self):
        print('Del function')


# a = A()

# a = object.__new__(A)
#
# print(a.__dict__)
# a.__init__('Title')
# print(a.__dict__)
#
# print(a._A__k)

# del a

class Values:
    def __init__(self, data):
        self.data: List = data

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    def append(self, value):
        self.data.append(value)

    def __iter__(self):
        yield from self.data


# values = Values([65, 48, 32])
# # print(values[0:1])
# # values[0:1] = [100, 56, 56]
# # print(values[::-1])
#
# # print(len(values))
#
#
# for i in values:
#     print(i)

class ContextManager:

    def __init__(self, file_name):
        self.fn = file_name

    def __enter__(self):
        print('Enter into file')
        try:
            self.f = open(self.fn)
        except Exception:
            print('Some error')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        try:
            self.f.close()
        except Exception:
            ...
        return False


with ContextManager('README.md') as f:
    print(f.read())



































