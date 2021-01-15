try:
    with open('lb.txt') as fo1, open('mb.txt') as fo2:
        print(fo1.read() + '\n' + fo2.read())
except FileNotFoundError:
        print('One of the given file does not exist in the given directory.')
