from dataclasses import dataclass


class Amount:

    def __init__(self, value: int, decimal: int):
        self.value = value
        self.decimal = decimal

    def __repr__(self):
        return f'Amount(value={self.value}, decimal={self.decimal})'


class Balance:

    def __init__(self, address: str, amount: Amount, asset: str):
        self.address = address
        self.amount = amount
        self.asset = asset


# b1 = Balance(
#     address='bitcoin_address',
#     amount=Amount(
#         value=123546,
#         decimal=8
#     ),
#     asset="BTC"
# )
#
#
# print(b1.__dict__)


# @dataclass
# class AmountData:
#     value: int
#     decimal: int
#
#
# @dataclass
# class BalanceData:
#     address: str
#     amount: Amount
#     asset: str


# b_data = BalanceData(
#     address='bitcoin_address',
#     amount=AmountData(
#         value=123546,
#         decimal=8
#     ),
#     asset="BTC"
# )
#
# b_data2 = BalanceData(
#     address='4563 1235 6541 2365',
#     amount=AmountData(
#         value=10,
#         decimal=0
#     ),
#     asset="USD"
# )
#
# print(b_data.__dict__)
# print(b_data2.__dict__)


class DataClassMeta(type):

    def __new__(meta_cls, name, bases, namespace, **kwargs):
        annotations = namespace.get('__annotations__')
        if annotations:
            init_code = meta_cls._make_init_(annotations)
            exec(init_code, globals(), namespace)

        return super().__new__(meta_cls, name, bases, namespace, **kwargs)

    @staticmethod
    def _make_init_(annotations: dict):
        # def __init__(self, value: int, decimal: int):
        #     self.value = value
        #     self.decimal = decimal

        lines = [
            'def __init__(self, {}):'.format(
                ', '.join(f'{arg}: {arg_type.__qualname__}' for arg, arg_type in annotations.items())
            )
        ]

        for arg, arg_type in annotations.items():
            lines.append(f'    self.{arg} = {arg}')

        print(lines)
        return '\n'.join(lines)


class DataClass(metaclass=DataClassMeta):
    ...


class AmountData(DataClass):
    value: int
    decimal: int


amount = AmountData(
    value=10,
    decimal=0
)

print(amount.__dict__)


# print(AmountData.__annotations__)


# @dataclass
# class BalanceData:
#     address: str
#     amount: Amount
#     asset: str