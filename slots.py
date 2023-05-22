
class A:
    __slots__ = [
        'a',
        'name',
        'age',
    ]

    def __init__(self):
        self.a = '56'
        self.name = 'Name'


a = A()
a.name = 'New name'
print(a.a, a.name)
a.data = "it's not posible do this"
print(a.__dict__)
#
# print(a.age)
a.age = 18
print(a.age)
# print(a.__dict__)


# c = [12, 56]
# print(type(c))
#
# c.new_attr = 'New attr'
