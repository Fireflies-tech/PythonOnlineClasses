# from abc import ABC, abstractmethod
#
#
# class A(ABC):
#
#     @abstractmethod
#     def run(self):
#         ...
#
#
# class B(A):
#
#     def run(self):
#         return 'Running'
#
#
# a = B()
#
# print(a.run())
from typing import List


# def f():
#     ...
#
# f.__arg__ = True
# print(type(f))
# print(f.__arg__)


def abstractmethod(fun):
    fun.__is_abstract__ = True
    return fun


def check_abstract_methods(cls) -> List:
    abc_funcs = []

    while isinstance(cls, ABCMeta):
        for key, val in vars(cls).items():
            if getattr(val, '__is_abstract__', False):
                abc_funcs.append(key)

        cls = cls.__mro__[1]

    return abc_funcs


class ABCMeta(type):

    def __call__(abc_cls, *args, **kwargs):
        abc_funcs = check_abstract_methods(abc_cls)

        if len(abc_funcs) > 0:
            raise TypeError(f'Need to implement following functions: [{"".join(abc_funcs)}]')

        return super().__call__(*args, **kwargs)


class ABC(metaclass=ABCMeta):
    ...


class A(ABC):

    @abstractmethod
    def run(self):
        ...


class B(A):
    ...


class G(B):
    ...


a = G()

print(G.__mro__)
