def count_the(filename):
    try:
        with open(filename) as f:
            text = f.read()
    except FileNotFoundError:
        print(filename + ' does not exist.')
    else:
        print(text.count('the'))


files = ['a1.txt', 'a2.txt', 'a3.txt', 'a4.txt']
for file in files:
    count_the(file)
