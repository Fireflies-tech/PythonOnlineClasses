
class Function:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a + self.b


f = Function(15, 6)
# print(f())
# f.a = 36
# print(f())
# print(dir(f))


# def power(func):
#     def wrapper(a, b):
#         res = func(a, b)
#         return res ** 2
#     return wrapper


class Power:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        res = self.func(a, b)
        return res ** 2


@Power
def add(a, b):
    return a + b


# r = add(5, 6)
#
# print(r)


class B:
    def __init__(self, name):
        self.name = name


class A:
    ...


instances = [A(), B('Pablo')]


# attr = 'surname'
#
# for instance in instances:
#     # print(hasattr(instance, 'name'))
#     if hasattr(instance, attr):
#         print(getattr(instance, attr))
#     else:
#         print(f'Name not found in {instance}')
#         # instance.name = 'Tadevos'
#         setattr(instance, attr, 'Tadevos')
#         print(getattr(instance, attr))
#


class GenNumbers:
    def __init__(self, n):
        self.n = n
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.n:
            num = self.current_num

            self.current_num += 1

            return num

        raise StopIteration


for i in GenNumbers(6):
    print(i)








