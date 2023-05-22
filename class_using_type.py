class A:
    a = 1
    b = 'b'

    def __init__(self, name):
        self.name = name

    def f(self):
        return self.b


def make_call(self):
    return f'Making a call ... {self.a}'


def B__init__(self, name):
    self.name = name


B = type('B', (), {
    'a': 1,
    'b': 'b',
    '__init__': B__init__,
    'f': lambda self: self.b,
    # 'make_call': make_call
})

a = A()
print(type(A))
print(a.a, a.f())

b = B('Ashot')
print(type(B))
print(b.a, b.f())
print(b.make_call())
print(b.name)


#
#
# def f(self):
#     return self.b
#
#
# def make_A_class(name: str, parents: Tuple):
#
#     namespaces = {
#         'a': 1,
#         'b': 'b',
#         'f': f
#     }
#
#     return type(name, parents, namespaces)
#
#
# NewAClass = make_A_class(
#     name='NewAClass',
#     parents=()
# )
#
# x = NewAClass()
#
# print(x.a, x.b, x.f())
# print(type(NewAClass))