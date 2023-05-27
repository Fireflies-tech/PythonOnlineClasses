from collections.abc import MutableSequence


class MutableString(MutableSequence):

    def __init__(self, value):
        super(MutableString, self).__init__()
        self.__value = bytearray(str(value), 'utf-8')

    def __delitem__(self, index):
        ...

    def __getitem__(self, index):
        ...

    def __len__(self):
        ...

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("<class 'MutableString'> indices must be integers or slices, not str")

        if abs(index) > len(self.__value) - 1:
            raise IndexError("<class 'MutableString'> assignment index out of range")

        if index < 0:
            index = len(self.__value) + index

        self.__value[index:index+1] = bytes(str(value), 'utf-8')

    def insert(self, index, value):
        ...

    def __str__(self):
        return self.__value.decode()

    def title(self):
        self.__value = bytearray(self.__value.decode().title(), 'utf-8')
        return self


if __name__ == '__main__':

    s = MutableString('Hello ')
    print(type(s))
    print(s)

    s[5] = ' World'  # s = 'HelloReplace'

    print(s)

    d = MutableString('vladimr')
    d.title()
    print(d)
