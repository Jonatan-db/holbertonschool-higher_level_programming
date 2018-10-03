#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
            self.size = size
            self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or value[0] < 0 or value[0] < 0 or\
                type(value) is not tuple or\
                type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size is 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.size + self.position[0]):
                    if j < self.position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()
