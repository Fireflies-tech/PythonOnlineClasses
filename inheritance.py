class DisableMultipleInheritanceMeta(type):

    def __new__(meta_cls, name, parents, namespace, **kwargs):
        if len(parents) > 1:
            raise ValueError('Multiple inheritance is not allowed.')
        return super().__new__(meta_cls, name, parents, namespace, **kwargs)


class A(metaclass=DisableMultipleInheritanceMeta):
    pass


class B:
    pass


class G(B):
    ...


class C(A):
    ...


class D(G, A):
    ...


class E(metaclass=DisableMultipleInheritanceMeta):
    ...


print(C)
print(type(C))

print(E)
print(type(E))

print(int)
print(type(int))
print(list)
print(type(list))
print(dict)
print(type(dict))












