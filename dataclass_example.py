class Amount:

    def __init__(self, value: int, decimal: int):
        self.value = value
        self.decimal = decimal

    def __repr__(self):
        return f'Amount(value={self.value}, decimal={self.decimal})'


class Balance:

    __slots__ = [
        'address',
        'amount',
        'asset'
    ]

    def __init__(self, address: str, amount: Amount, asset: str):
        self.address = address
        self.amount = amount
        self.asset = asset

    def __repr__(self):
        return f'Balance(address: {self.address}, amount={self.amount}, asset={self.asset})'

    def __eq__(self, other):
        ...

    def __le__(self, other):
        ...

    def __ge__(self, other):
        ...


b1 = Balance(
    address='bitcoin_address',
    amount=Amount(
        value=123546,
        decimal=8
    ),
    asset="BTC"
)
b2 = Balance(
    address='acba/4356-5621-6544-5621',
    amount=Amount(
        value=1000,
        decimal=0
    ),
    asset="EUR"
)

#
# b3 = {
#     "address": "acba/4356-5621-6544-5621",
#     "asset": "EUR",
#     "amount": {
#         "value": 1000,
#         'decimal': 0
#     },
# }
#
# print(b1.__dict__)
# print(b2.__dict__)
# print(b2.asset)
#
# print(b3.get('address'))


from dataclasses import dataclass


@dataclass
class AmountData:
    value: int
    decimal: int


@dataclass(frozen=True, slots=True)
class BalanceData:
    address: str
    amount: Amount
    asset: str


# b_data = BalanceData(
#     address='ether',
#     amount=AmountData(
#         value=123546,
#         decimal=8
#     ),
#     asset="ETH"
# )
#
# print(b_data)


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


def _make_init_(annotations: dict):
    """
    :param annotations: {'value': <class 'int'>, 'decimal': <class 'int'>}
    :return: init code
    # def __init__(self, value: int, decimal: int):
    #     self.value = value
    #     self.decimal = decimal
    """
    lines = []
    args = []
    for arg, annot in annotations.items():
        args.append(f'{arg}: {annot.__qualname__}')
        lines.append(f'    self.{arg} = {arg}')

    lines = [f"def __init__(self, {', '.join(args)}):"] + lines

    return '\n'.join(lines)


class DataClassMeta(type):

    def __new__(meta_cls, name, bases, namespace, **kwargs):
        annotations = namespace.get('__annotations__')
        if annotations:
            init_code = _make_init_(annotations)
            exec(init_code, globals(), namespace)

        return super().__new__(meta_cls, name, bases, namespace, **kwargs)


class DataClass(metaclass=DataClassMeta):
    ...


class AmountData(DataClass):
    value: int
    decimal: int

    def __repr__(self):
        return f'Amount(value={self.value}, decimal={self.decimal})'


class BalanceData:
    address: str
    amount: AmountData
    asset: str


amount1 = AmountData(value=100, decimal=8)
amount2 = AmountData(value=200, decimal=8)

print(amount1)
print(amount2)



# print(BalanceData.__annotations__)
