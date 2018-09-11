def uppercase(str):
    for i in str:
        convert = ord(i)
        if convert >= 97 and convert <= 122:
            convert -= 32
        print("{}".format(chr(convert)), end='')
    print('')
