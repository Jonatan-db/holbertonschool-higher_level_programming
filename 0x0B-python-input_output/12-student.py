#!/usr/bin/python3
""" expands on #11 """


class Student():
    """ this expands on the previous function script """

    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dics """
        if attrs is None:
            return self.__dict__
        dic = {}
        for a in attrs:
            if a is "first_name":
                dic[a] = self.first_name
            elif a is "last_name":
                dic[a] = self.last_name
            elif a is "age":
                dic[a] = self.age
            else:
                pass
        return dic
