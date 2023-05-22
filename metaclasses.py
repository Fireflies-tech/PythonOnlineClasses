
# Metaclass

# 1 method
# class Question1:
#
#     def the_answer(self):
#         return 50
#
#
# class Question2:
#
#     def the_answer(self):
#         return 50
#
#
# class Question3:
#
#     def the_answer(self):
#         return 50
#

#  2 method
# class Answer:
#     def the_answer(self):
#         return 50
#
#
# class Question1(Answer):
#     pass
#
#
# class Question2(Answer):
#     pass
#
#
# class Question3(Answer):
#     pass
#
#
# x = input('Do you need "the answer"? (y/N)')
#
# required = False
# if x == 'y':
#     required = True
#
#
# def the_answer(self):
#     return 50
#
#
# class Question1:
#     pass
#
# if required:
#     Question1.the_answer = the_answer
#
#
# class Question2:
#     pass
#
# if required:
#     Question2.the_answer = the_answer
#
# class Question3:
#     pass
#
# if required:
#     Question3.the_answer = the_answer

#
# x = input('Do you need "the answer"? (y/N)')
#
# required = False
# if x == 'y':
#     required = True
#
#
# def the_answer(self):
#     return 50
#
#
# def bind_answer(cls):
#     if required:
#         cls.the_answer = the_answer
#
#
# class Question1:
#     pass
#
# bind_answer(Question1)
#
#
# class Question2:
#     pass
#
# bind_answer(Question2)
#
#
# class Question3:
#     pass
#
# bind_answer(Question3)

#
# # x = input('Do you need "the answer"? (y/N)')
#
# x = 'y'
#
# required = False
# if x == 'y':
#     required = True
#
#
# def the_answer(self):
#     return 50
#
#
# def bind_answer(cls):
#     if required:
#         cls.the_answer = the_answer
#     return cls
#
#
# @bind_answer
# class Question1:
#     pass
#
#
# @bind_answer
# class Question2:
#     pass
#
#
# @bind_answer
# class Question3:
#     pass
#
#
# class A(Question3):
#     pass


# q1 = Question1()
# print(q1.the_answer())
#
# q2 = Question2()
# print(q2.the_answer())


# print(type(Question1))
# print(type(int))


# class Meta(type):
#     def __new__(metacls, clsname, superclasses, attribute_dict):
#         # print(f'{clsname=}')
#         # print(f'{superclasses=}')
#         # print(f'{attribute_dict=}')
#         return super().__new__(metacls, clsname, superclasses, attribute_dict)
#
#
# class Question4(metaclass=Meta):
#     pass
#
#
# print(type(Question1))
# print(type(Question4))



# x = input('Do you need "the answer"? (y/N)')
#
#
# required = False
# if x == 'y':
#     required = True
#
#
# def the_answer(self):
#     return 50
#
#
# class AnswerMeta(type):
#     def __init__(metacls, cls_name, superclasses, attr_dict):
#         if required:
#             metacls.the_answer = the_answer
#
#
# class Question1(metaclass=AnswerMeta):
#     pass
#
#
# class Question2(metaclass=AnswerMeta):
#     pass
#
#
# class Question3(metaclass=AnswerMeta):
#     pass
#
#
# q1 = Question1()
# print(q1.the_answer())
#
# q2 = Question2()
# print(q2.the_answer())
#


# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#
#         return cls._instances[cls]


class SingletonMeta:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class DBConnectionSingleton(SingletonMeta):
    pass


print(DBConnectionSingleton._instance)
print(DBConnectionSingleton())
print(DBConnectionSingleton())
print(DBConnectionSingleton())
print(DBConnectionSingleton())
print(DBConnectionSingleton())


# db_connect_1 = DBConnectionSingleton()
# db_connect_2 = DBConnectionSingleton()
#
# print(db_connect_1)
# print(db_connect_2)

# print(db_connect_1 == db_connect_2)


class DBConnection:
    pass


# db_connect_1 = DBConnection()
# db_connect_2 = DBConnection()
#
# print(db_connect_1)
# print(db_connect_2)
#
# print(db_connect_1 == db_connect_2)



