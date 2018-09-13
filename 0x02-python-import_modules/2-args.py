#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    else:
        if length == 2:  # case for 1 argument
            print("1 argument:")
        elif length > 2:  # case for more than 1
            print("{} arguments:".format(length - 1))
        for i in range(1, length):  # print out the arguments
            print("{}: {}".format(i, sys.argv[i]))
