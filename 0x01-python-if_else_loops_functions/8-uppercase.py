def uppercase(str):
    array = []
    count = 0
    for i in str:
        if i >= 'a' and i <= 'z':
            array.append(chr(ord(i) - 32))
        else:
            array.append(i)
        print(array[count], end='')
        count += 1
    print('')
