from django.test import TestCase

# Create your tests here.


# def foo(action=None,**kwargs):
#     print(action)
#     print(kwargs)
#
# # foo({"a":1},b=2,c=3)
# # foo(b=2,c=3)
# foo(**{"d":"5"})
# foo({"d":"5"})
# 总结： **字典等同于关键字传参




#
# def bar(*args):
#     pass
#
# bar([1,2,3])
# bar(*[1,2,3]) # foo(1,2,3)


#
# print(3 and 0)
# print(0 and 2)
# print(0 or 1)
# print(4 or 1)


class Person(object):

    def __init__(self,name):
        self.name=name


    def __getattr__(self, item):
        print("item",item)


    def dream(self):
        print("dreaming....")

alex=Person("alex")

# alex.dream()

alex.pppp

